from django.shortcuts import render,redirect,get_object_or_404
from BloodStream.models import bloodrequest,donors,User

from BloodStream.forms import donorform,bloodrequestform,RegsitrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def homepage(request):
    return render(request,"index.html")


def authview(request):
    form=RegsitrationForm()
    if request.method=='POST':
        form=RegsitrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.is_staff=True
            user.save()
            return homepage(request)

    return render(request,'registration/signup.html',{'forms':form})

def login_view(request):
    form=AuthenticationForm()
    if request.method=="POST":
        form=AuthenticationForm(request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
   
    return render(request,'registration/login.html',{"form":form})

def logout(request):
    return redirect('home')

         
@login_required(login_url='login')
def donor_login(request):
   
    donor_user=donors.objects.filter(user=request.user).exists()
    if  donor_user:
        return redirect(donor_dashboard)
    else:
        if request.method=="POST":
            form=donorform(request.POST)
            if form.is_valid():
              donor= form.save(commit=False)
              donor.user=request.user
              donor.save()
              return homepage(request)
            else:
                print(form.errors)
                return render(request,'donorregistration.html',{"form":form})
        else:
            form=donorform()


    return render(request,"donorregistration.html",{'form':form})
@login_required(login_url='login')
def blood_request(request):
    form=bloodrequestform()
    if request.method=="POST":
        form=bloodrequestform(request.POST)
        if form.is_valid():
            blood_req=form.save()
            blood_req.user=request.user
            blood_req.save()
        return homepage(request)
    return render(request,"searchblood.html",{'form':form})

def available_requests(request):
    context=bloodrequest.objects.filter(~Q(user_id = request.user.id),status='pending').order_by('-created_at')
    paginator=Paginator(context,10)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
   

    return render(request,"requestdetails.html",{'page_obj':page_obj,'requests':context})

@login_required(login_url='login')
def approve_request(request,id):
    donor=get_object_or_404(donors,user=request.user)
    blood_request=get_object_or_404(bloodrequest,id=id)
   
    if blood_request.status=='pending':
        blood_request.status='approved'
        blood_request.donor=donor
        blood_request.save()

    return homepage(request)
def delete_request(request,id):
    req = bloodrequest.objects.get(id=id)
    req.delete()
    return render(request,'receiver_dashboard.html')
def update_request(request,id):
    req=bloodrequest.objects.get(id=id)
    
    if request.method=="POST":
        updateform=bloodrequestform(request.POST,instance=req)
        if updateform.is_valid():
            updateform.save()
            return redirect('home')
    else:
        updateform=bloodrequestform(instance=req)
            
    return render(request,'update.html',{'form':updateform})



@login_required(login_url='login')
def donor_dashboard(request):
   
    donor_id=donors.objects.filter(user=request.user).exists()
    
    if donor_id:
        donor=get_object_or_404(donors,user=request.user)
        requests=bloodrequest.objects.filter(status='approved',donor_id=donor.id)
        context={'requests':requests, 'donor': donor}
        return render(request,'donor_dashboard.html',context)
    else:
        messages.warning=(request,"you are not a donor yet please be a donor!!")
       
        return render(request,'donor_dashboard.html')
def receiver_dashboard(request):
    if request.user.is_authenticated:

        requests=bloodrequest.objects.filter(user=request.user)
    else:
        return redirect('login')
    

    return render(request,'receiver_dashboard.html',{'requests':requests})

def about_page(request):
    return render(request,"about_page.html")

class pagination(ListView):
    model=bloodrequest 
    template_name='responses.html'
    context_object_name='requests'

    def query_set(self):
        get_query=super().query_set()
        status=self.request.GET.get('status')
        if status:
            get_query=get_query.filter(status='pending')
        return get_query
