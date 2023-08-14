from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import attendance

# Create your views here.

def login_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('upload')
    else:
        return render(request, 'Login.html')

def upload(request):
    if request.user.is_authenticated:
        return render(request, 'Upload.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'Upload.html')
        else:
            return HttpResponseRedirect('/')
        
def success(request):
    if request.user.is_authenticated:
        name = request.POST['name']
        roll = request.POST['rollNumber']
        try:
            res = attendance.objects.get(roll=roll)
            attendance.objects.filter(roll=roll).update(name=name, mrec=0, dt='1970-01-01 00:00:00')
        except:
            entry = attendance.objects.create(roll=roll, name=name, mrec=0, dt='1970-01-01 00:00:00')
            entry.save()
        return HttpResponseRedirect('upload')
    
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')

