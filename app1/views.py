from django.shortcuts import render
from .models import *


# Create your views here.
def showindex(request):
    return render(request,'index.html')


def admin_register(request):
    return render(request,'admin_register.html')


def admin_register_details(request):
    name=request.POST.get('name')
    username=request.POST.get('username')
    password=request.POST.get('password')
    AdminRegister(name=name,username=username,password=password).save()
    message='successfully registered'
    return render(request,'admin_register.html',{'message':message})


def admin_login(request):
    return render(request,'admin_login.html')


def admin_login_details(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    login=AdminRegister.objects.filter(username=username,password=password)
    if login:
        return render(request,'home.html')
    else:
        message='invalid login details'
        return render(request,'admin_login.html',{'message1':message})


def sbi_branch(request):
    sbi=SbiManager.objects.all()
    return render(request,'sbi.html',{'sbi':sbi})


def icici_branch(request):
    icici=IciciManager.objects.all()
    return render(request,'icici.html',{'icici':icici})


def manager_login(request):
    return render(request,'manager_login.html')


def manager_registration(request):
    return render(request,'manager_register.html')

def manager_register_details(request):
    name=request.POST.get('name')
    username=request.POST.get('username')
    password=request.POST.get('password')
    location=request.POST.get('location')
    SbiManager(manager_name=name,username=username,password=password,location=location).save()
    message = 'successfully registered'
    return render(request,'manager_register.html',{'message':message})


def brach_managers(request):
    return render(request,'manager.html')


def icici_manager(request):
    return render(request,'icici_manager.html')


def icici_manager_registration(request):
    return render(request,'icici_manager_register.html')


def icici_manager_register_details(request):
    name = request.POST.get('name')
    username = request.POST.get('username')
    password = request.POST.get('password')
    location = request.POST.get('location')
    IciciManager(manager_name=name, username=username, password=password, location=location).save()
    message = 'successfully registered'
    return render(request,'icici_manager_register.html',{'message':message})


def manager_login_details(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    login=SbiManager.objects.filter(username=username,password=password)
    if login:
        sbi = SbiManager.objects.all()
        return render(request, 'sbi.html', {'sbi': sbi})
    else:
        message = 'invalid login details'
        return render(request,'manager_login.html',{'message':message})


def icici_manager_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    login = IciciManager.objects.filter(username=username, password=password)
    if login:
        icici = IciciManager.objects.all()
        return render(request, 'icici.html', {'icici': icici})
    else:
        message = 'invalid login details'
        return render(request,'icici_manager.html',{'message':message})