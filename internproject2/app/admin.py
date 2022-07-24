from django.contrib import admin
from app.models import Card
# Register your models here.
@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display=['id','heading','sub_heading','description','image']