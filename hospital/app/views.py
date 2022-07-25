from turtle import st
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from app.forms import LoginForm,HospitalForm,ProfileForm
from app.models import User,Profile
# from app.models import Hospital
from django.contrib import messages
from django.contrib.auth.models import Group

# def signup(request):
#     try:
#         if request.method=='POST':
#             fm=HospitalForm(request.POST)
#             if fm.is_valid:
#                 user=fm.save()
#                 group=Group.objects.get(name='Member')
#                 user.groups.add(group)
#                 fm=HospitalForm()
#                 messages.success(request,'congrats successfully signup')
#         else:
#             fm=HospitalForm()
#         return render(request,'app/signup.html',{'form':fm})
#     except:
#         messages.warning(request,'Password not match')
#         return HttpResponseRedirect('/')

def signup(request):
    if not request.user.is_authenticated:
        try:
            if request.method=='POST':
                fm=HospitalForm(request.POST)
                if fm.is_valid:
                    user=fm.save()
                    group=Group.objects.get(name='Member')
                    user.groups.add(group)
                    fm=HospitalForm()
                    messages.success(request,'congrats successfully signup')
            else:
                fm=HospitalForm()
            return render(request,'app/signup.html',{'form':fm})
        except:
            messages.warning(request,'Password not match')
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/dashboard/')

def userlogin(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'congrats successfully Login')
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm=LoginForm()
        return render(request,'app/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')

def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# def dashboard(request):
#     # print("request data: ", request.user)
#     # print("request data: ", request.user.id)
#     if request.user.is_superuser:
#         # posts=Profile.objects.filter(user=request.user.id)
#         posts=Profile.objects.all()
#         print("posts: ", posts)
#         return render(request,'app/dashboard.html',{'posts':posts,'name':request.user.first_name,'name2':request.user.last_name})
#     if request.user.is_authenticated:
#         # posts=Profile.objects.all()
#         posts=Profile.objects.filter(user=request.user.id)
#         # print("posts: ", posts)
#         return render(request,'app/dashboard.html',{'posts':posts,'name':request.user.first_name,'name2':request.user.last_name})
#     else:
#         return HttpResponseRedirect('/login/')

def dashboard(request):
    try:
    # print("request data: ", request.user)
    # print("request data: ", request.user.id)
        if request.user.is_superuser:
        # posts=Profile.objects.filter(user=request.user.id)
            posts=Profile.objects.all()
            # print("posts: ", posts)
            return render(request,'app/dashboard.html',{'posts':posts,'name':request.user.first_name,'name2':request.user.last_name})
        if request.user.is_authenticated:
        # posts=Profile.objects.all()
            posts=Profile.objects.filter(user=request.user.id)
        # print("posts: ", posts)
            return render(request,'app/dashboard.html',{'posts':posts,'name':request.user.first_name,'name2':request.user.last_name})
        else:
            return HttpResponseRedirect('/login/')
    except:
        return HttpResponseRedirect('/dashboard/')


def addpost(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=ProfileForm(request.POST)
            if fm.is_valid():
                user=fm.cleaned_data['user']
                profile_pic=fm.cleaned_data['profile_pic']
                type=fm.cleaned_data['type']
                line=fm.cleaned_data['line']
                city=fm.cleaned_data['city']
                state=fm.cleaned_data['state']
                pincode=fm.cleaned_data['pincode']
                print('user_id: ',request.user.id)
                print('user2: ',user.id)
                if request.user.id==user.id:
                    pst=Profile(user=user,profile_pic=profile_pic,type=type,line=line,city=city,state=state,pincode=pincode)
                    pst.save()
                    fm=ProfileForm()
                else:
                    messages.success(request,'Incorrect User')
                    return HttpResponseRedirect('/addpost/')
        else:
            fm=ProfileForm()
        return render(request,'app/addpost.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def updatepost(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Profile.objects.get(pk=id)
            fm=ProfileForm(request.POST,instance=pi)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            pi=Profile.objects.get(pk=id)
            fm=ProfileForm(instance=pi)
        return render(request,'app/updatepost.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')

def deletepost(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Profile.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')