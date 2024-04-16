from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Contact_Us, CarUser
from django.contrib.auth.decorators import login_required
from .models import Car , Booking
from django.contrib.auth.models import User
from .forms import BookingForm



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
    return render(request,'client.html')

# @login_required(login_url='login')
def gallery(request):
    cars = Car.objects.all()

    search_brand = request.GET.get('search_brand')
    search_model = request.GET.get('search_model')
    search_max_price = request.GET.get('search_max_price')

    if search_brand:
        cars = cars.filter(brand__icontains=search_brand)
    if search_model:
        cars = cars.filter(model__icontains=search_model)
    if search_max_price:
        cars = cars.filter(price__lte=search_max_price)

    context = {
        'cars': cars
    }
    return render(request, 'gallery.html', context)



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





# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST.get('UserName')
#         password = request.POST.get('Password')

#         # if username and password:
#         user = authenticate(request,username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('learning')
#             messages.error(request, 'login sucsses.')
#         else:
#                 messages.error(request, 'Invalid username or password.')
#     #  else:
#             # messages.error(request, 'Please provide both username and password.')
        
#         # return redirect('learning')
#     else:
#         return render(request, 'login.html')
#     return HttpResponse("Method not allowed", status=405)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('UserName')  
        password = request.POST.get('Password') 

        user = authenticate(request, username=username, password=password)  
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('learning')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        return render(request, 'login.html')

    return HttpResponse("Method not allowed", status=405)

def submit_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Process the form data and save the booking
            form.save()
            # Redirect to a thank you page or any other appropriate page
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})



def logout_user(request):
    logout(request)
    return redirect('learning')




def add_car(request):
    if request.method == 'POST':
        # Extract data from the POST request
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        year = request.POST.get('year')
        car_type = request.POST.get('car_type')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        # Create a new Car object and save it to the database
        car = Car.objects.create(
            brand=brand,
            model=model,
            year=year,
            car_type=car_type,
            price=price,
            image=image
        )
        
        return redirect('gallery')  # Redirect to gallery page after adding the car

    return render(request, 'add_car.html')



def submit_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Process the form data and save the booking
            form.save()
            # Redirect to the booking confirmation page
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})

def booking_success(request):
    return render(request, 'booking_success.html')

