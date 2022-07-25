from django.contrib import admin
from app.models import Profile
# Register your models here.
@admin.register(Profile)
class HospitalAdmin(admin.ModelAdmin):
    # list_display=['id','first_name','last_name','profile_pic','username','email','type']
    list_display=['id','user','profile_pic','line','city','state','pincode']