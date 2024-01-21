from django.shortcuts import render , redirect
from .models import Member
from django.contrib.auth.models import auth , User
from django.contrib import messages
# Create your views here.

def Home(request):
    return render(request , 'home.html')


def Register(request):
    if request.method == "POST":
        name = request.POST['membername']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']

        if password == c_password and len(password) != 0 and len(name) != 0 and len(email) != 0 :
            if Member.objects.filter(email = email).exists():
                messages.info(request , " This Email is already registered.")
                return redirect('register')
            
            else:
                new_member = Member.objects.create(name = name , email = email , password = password)
                new_member.save()
                messages.info(request , "Member Registered Successfully..")
                return redirect('register')

        else:
            messages.info(request , "Both passwords are not matching ... or you have an empty field") 
            return redirect('register')  
    
    return render(request , 'register.html')


def Login(request):
    
    return render(request , 'login.html')

def ChatHome(request):
    member = request.POST['']
    return render(request , 'chathome.html')