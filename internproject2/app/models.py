from django.db import models

# Create your models here.
class Card(models.Model):
    image=models.CharField(max_length=100)
    heading=models.CharField(max_length=30)
    sub_heading=models.CharField(max_length=30)
    description=models.TextField(max_length=30)