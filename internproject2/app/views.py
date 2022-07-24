from django.shortcuts import render
from django.views import View
from app.forms import CardForm
from django.contrib import messages
from app.models import Card
# Create your views here.
# def home(request):
#     return render(request,'app/home.html')

class home(View):
    def get(self,request):
        card=Card.objects.all()
        return render(request,'app/home.html',{'card':card})

# def home(request):
#     if request.method=='GET':
#         card=Card.objects.all()
#         return render(request,'app/home.html',{'card':card})