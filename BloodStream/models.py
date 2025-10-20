from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Profile(models.Model):
#     ROLE_CHICES=[
#         ('donor','Donor')
#         ('receiver','receiver')
#     ]
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
#     role=models.CharField(max_length=20,choices=ROLE_CHICES)
#     blood_group=models.CharField(max_length=5)
#     phone=models.CharField(max_length=15)
#     def __str__(self):
#         return self.user.username
class donors(models.Model):
    BLOOD_GROUPS=[
        ("A+","A+"),
        ("B+","B+"),
        ("A-","A-"),
        ("B-","B-"),
        ("AB+","AB+"),
        ("AB-","AB-"),
        ("O+","O+"),
        ("O-","O-"),

    ]
    GENDERS=[
        ("Male","Male"),
        ("Female","Female"),
        ("Other","Other"),
    ]

    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='donor')
    full_name=models.CharField(max_length=50)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=10,choices=GENDERS)
    Blood_Group=models.CharField(max_length=10,choices=BLOOD_GROUPS)
    Dist=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    village=models.CharField(max_length=50)
    pincode=models.CharField(max_length=6)
    contact=models.CharField(max_length=10)
    email=models.EmailField(unique=True)
    registered_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name
class bloodrequest(models.Model):
    BLOOD_GROUPS=[
        ("A+","A+"),
        ("B+","B+"),
        ("A-","A-"),
        ("B-","B-"),
        ("AB+","AB+"),
        ("AB-","AB-"),
        ("O+","O+"),
        ("O-","O-"),]
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    patient_name=models.CharField(max_length=20)
    Blood_Group=models.CharField(max_length=10,choices=BLOOD_GROUPS)
    Reason=models.CharField(max_length=200)
    Dist=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    Contact=models.CharField(max_length=15)
    status=models.CharField(max_length=20,default='pending')
    created_at=models.DateTimeField(auto_now_add=True)
    donor=models.ForeignKey(
        donors,null=True,on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.patient_name

    



