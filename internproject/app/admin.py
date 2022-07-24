from django.contrib import admin
from app.models import SimpleForm
# Register your models here.
@admin.register(SimpleForm)
class SimpleFormAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','gender','email','address','pincode']