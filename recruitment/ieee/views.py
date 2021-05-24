from django.shortcuts import render

# Create your views here.
from ieee.forms import infoForm
from ieee import models
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import registerit

def LoginPage(request):
    data={}
    if request.method=='POST':
        username=request.POST['Username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect('/ieee/home-page/')
        else:
            data['error']='Username or Password is incorrect'
            return render(request,'ieee/LoginPage.html',data)
    else:
        return render(request,'ieee/LoginPage.html',data)

def LogoutPage(request):
    logout(request)
    return HttpResponseRedirect('/ieee/login-page/')

def SignupPage(request):
    if request.method=='POST':
        form=registerit(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ieee/login-page/')
    else:
        form=registerit()
    return render(request,'ieee/SignupPage.html',{'form':form})

@login_required(login_url='/ieee/login-page/')
def HomePage(request):
    return render(request,'ieee/HomePage.html')

@login_required(login_url='/ieee/login-page/')
def DeletePage(request):
    infoid=request.GET['infoid']
    info=models.info.objects.filter(id=infoid)
    info.delete()
    return HttpResponseRedirect('/ieee/candidate-page/')

@login_required(login_url='/ieee/login-page/')
def EditPage(request):
    infoid=request.GET['infoid']
    info=models.info.objects.get(id=infoid)
    fields={'name':info.name,'gender':info.gender,'dob':info.dob,'branch':info.branch,'phone':info.phone,'email':info.email}
    form=infoForm(initial=fields)
    return render(request,'ieee/EditPage.html',{'form':form,'info':info})

@login_required(login_url='/ieee/login-page/')
def Edit(request):
    if request.method=="POST":
        form=infoForm(request.POST)
        info=models.info()
        info.id=request.POST['infoid']
        info.name=form.data['name']
        info.gender=form.data['gender']
        info.dob=form.data['dob']
        info.branch=form.data['branch']
        info.phone=form.data['phone']
        info.email=form.data['email']
    info.save()
    return HttpResponseRedirect("/ieee/candidate-page/")

@login_required(login_url='/ieee/login-page/')
def RegisterPage(request):
    form=infoForm()
    return render(request,'ieee/RegisterPage.html',{'form':form})

@login_required(login_url='/ieee/login-page/')
def Add(request):
    if request.method=="POST":
        info=models.info()
        form=infoForm(request.POST)
        info.name=form.data['name']
        info.gender=form.data['gender']
        info.dob=form.data['dob']
        info.branch=form.data['branch']
        info.phone=form.data['phone']
        info.email=form.data['email']
    info.save()
    return HttpResponse("You Are Successfully Registered <br> <a href='/ieee/home-page/'>Click Here</a>")

@login_required(login_url='/ieee/login-page/')
def InstructionPage(request):
    return render(request,'ieee/InstructionPage.html')

@login_required(login_url='/ieee/login-page/')
def CandidatePage(request):
    info=models.info.objects.all()
    return render(request,'ieee/CandidatePage.html',{'info':info})
