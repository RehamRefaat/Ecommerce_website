from django.shortcuts import render
from .models import *
from .views import *
from django.contrib.auth import authenticate,login as loginauth
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request,"account/login.html")
    else:
        username=request.POST['txt']
        userpassword=request.POST['pswd']
        myaccount=Account.objects.filter(UserName=username,UserPassword=userpassword)
        if len(myaccount)>0:
            useradmain=authenticate(username=username,password=userpassword)
            if (useradmain is not None):
                loginauth(request, useradmain)
                request.session['name']=myaccount[0].UserName
                return HttpResponseRedirect('/account/home/')
            else:
                context = {}
                context['massage'] = 'invalid admin'
                return render(request, '/account/login.html', context)
        else:
            context={}
            context['massage']='invalid username or password'
            return render(request, 'account/login.html',context)

def register(request):
    if request.method=='GET':
        return render(request,"account/register.html")
    else:
        username = request.POST['txt']
        userpassword = request.POST['pswd']
        usermail = request.POST['email']
        Account.objects.create(UserName=username,UserPassword=userpassword,UserEmail=usermail)
        User.objects.create_user(username=username,password=userpassword,email=usermail,is_staff=True,is_active =True)
        return HttpResponseRedirect('/account/login/')