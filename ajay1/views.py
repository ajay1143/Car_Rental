from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['Name']
        email = request.POST.get('Email')  
        contact = request.POST.get('Contact')  
        message = request.POST.get('Message')
        Contact_Us.objects.create(name=name, email=email, contact=contact, message=message)
    return render(request, 'contact.html')


def client(request):
    return render(request, 'client.html')


def gallery(request):
    return render(request, 'gallery.html')


def services(request):
    return render(request, 'services.html')


def data_submit(request):
    if request.method == 'POST':
        name = request.POST['Name']
        email = request.POST.get('Email')  
        contact = request.POST.get('Contact')  
        message = request.POST.get('Message')
        Contact_Us.objects.create(name=name, email=email, contact=contact, message=message)
    return redirect("learning")


def register_user(request):
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST.get('UserName')
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        cpassword = request.POST.get('Cpassword')
        phone = request.POST.get('phone')
        
        if not (username and email and password and cpassword and phone):
            return HttpResponse('All fields are required!')

        if password != cpassword:
            return HttpResponse('Passwords do not match!')
        
        user = CarUser.objects.create(
            username=username,
            email=email,
            password=password,
            phone=phone
        )
        user.save()
        
        return HttpResponse('User registered successfully!')
    else:
        return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('learning')  # Redirect to the contact page
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login') 
    else:
        return render(request, 'login.html')
