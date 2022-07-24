from django.shortcuts import render
from app.forms import SimpleFormData
from django.contrib import messages
# Create your views here.
def FormView(request):
    if request.method=='POST':
        form=SimpleFormData(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Congratulations!! your data is successfull submited')
            form=SimpleFormData()
    else:
        form=SimpleFormData()
    return render(request,'app/home.html',{'form':form})