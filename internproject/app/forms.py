from socket import fromshare
from django import forms
from app.models import SimpleForm
class SimpleFormData(forms.ModelForm):
    first_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    # gender=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    address=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    # pincode=forms.IntegerField(widget=forms.IntegerField(attrs={'class':'form-control'}))
    class Meta:
        model=SimpleForm
        fields=['first_name','last_name','gender','email','address','pincode']
        # widgets={
        #     'pincode':forms.IntegerField(attrs={'class':'form-control'})
        # }