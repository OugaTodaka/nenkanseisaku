from django.http import *
from django.shortcuts import render
from .models import CustomUser
from django.contrib.auth import login,logout

def signup_sys(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        new_user = CustomUser(username=username,password=password)
        new_user.save()
        user = CustomUser.objects.get(username=username)
        login(request,user)
        return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/signup_faild')

def signin_sys(request):
    username = request.POST['username']
    password = request.POST['password']

    try:
        user = CustomUser.objects.get(username=username)
    except CustomUser.DoesNotExist:
        return HttpResponseRedirect('/faild')

    if user.password == password:
        login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/signin_faild')

def signout(request):
    logout(request)
    return HttpResponseRedirect('/')

def signin_faild(request):
    return render(request,'signin_faild.html')

def signup_faild(request):
    return render(request,'signup_faild.html')