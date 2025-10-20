from BloodStream.models import donors,bloodrequest
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class donorform(forms.ModelForm):
    class Meta():
        model=donors
        fields=['full_name','Age','Gender','Blood_Group','Dist','city','village','pincode','contact','email']

    def clean_Age(self):
        
        Age=self.cleaned_data.get('Age')
        if Age and Age<18:
            raise forms.ValidationError("you are must be atleast 18 years old")
        return Age

class bloodrequestform(forms.ModelForm):
    class Meta():
        model=bloodrequest
        fields=['patient_name','Blood_Group','Reason','Dist','City','Contact',]   



class RegsitrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']
    
    # def clean(self):
    #     clean_data=super().clean()
    #     username=clean_data.get('username')
    #     password1=clean_data.get('password1')
    #     password2=clean_data.get('password2')
    #     if password1 != password2:
    #         if username.lower() in password1.lower():
    #            self.add_error(None,'password doesnot contain username')
    #     return clean_data