from rest_framework import serializers
from app.models import SimpleForm
class SimpleFormSerializer(serializers.ModelSerializer):
    class Meta:
        model=SimpleForm
        fields=['id','first_name','last_name','gender','email','address','pincode']