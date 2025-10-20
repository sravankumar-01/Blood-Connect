from django.contrib import admin
from BloodStream.models import donors,bloodrequest

# Register your models here.
admin.site.register(donors)
admin.site.register(bloodrequest)