
from django.urls import path
from BloodStream.views import*

urlpatterns = [
   
    path("home",homepage,name="home"),
    path("donorlogin",donor_login,name="donorlogin"),
    path('request',blood_request,name='searchblood'),
    path("availablerequests",available_requests),
    path('requestdetails',pagination.as_view(),),
    path('approve/<int:id>',approve_request,name='approve'),
    path('donordashboard',donor_dashboard,name='donordashboard'),
    path('receiverdashboard',receiver_dashboard,name='receiverdashboard'),
    path('signup',authview,name='signup'),
    path('login',login_view,name="login"),
    path('logout',logout,name="logout"),
    path('about',about_page,name='about'),
    path('deletereq/<int:id>',delete_request,name="deletereq"),
    path('updatereq/<int:id>',update_request),

]