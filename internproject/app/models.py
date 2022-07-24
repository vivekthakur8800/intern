from django.db import models

# Create your models here.
GENDER_CHOICES={
    ('M','Male'),
    ('F','Female'),
    ('T','Transgender')
}
class SimpleForm(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    gender=models.CharField(choices=GENDER_CHOICES,max_length=20)
    email=models.EmailField()
    address=models.CharField(max_length=50)
    pincode=models.IntegerField()