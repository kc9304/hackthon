from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Admin
from django.contrib.auth.models import User


# Create your views here.
def base(request):
    return render(request,'logout/home/home.html')

def checklogin(request):
    uname = request.POST["uname"]
    password = request.POST["pwd"]
    flag = Admin.objects.filter(Q(username=uname) & Q(password=password))
    request.session['uname'] = uname
    print(flag)
    if flag and uname == "KC":
        return redirect('phome')
    if flag:
        return redirect('lhome')
    else:
        return redirect('home')

def profile(request):
    uname = request.session.get('uname')

    context = {
        'uname': uname,
    }

    return render(request, 'login/home/profile.html',context)

def addregister(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['pwd']
        email=request.POST['email']
        new_id = Admin(username=uname,password=password,email=email)
        request.session['uname'] = uname
        new_id.save()
        return redirect('lhome')