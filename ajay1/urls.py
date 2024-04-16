from django.contrib import admin
from django.urls import path
from ajay1 import views
from django.conf import settings
from django.conf.urls.static import static
from .views import submit_booking ,booking_success 

urlpatterns = [
    path('', views.index,name='learning'),
    path('about/', views.about,name ='about'),
    path('contact/', views.contact,name ='contact'),
    path('client/', views.client,name ='client'),
    path('services/', views.services,name ='services'),
    path('gallery/', views.gallery,name ='gallery'),
    path("data_submit/",views.data_submit,name ='data_submit'),
    path("register/",views.register_user,name ='register'),
    path('login/',views.login_user,name ='login'),
    path('logout/',views.logout_user,name ='logout'),
    path('cars/',views.add_car,name ='cars'),
    path('submit_booking/', submit_booking, name='submit_booking'),
    path('booking_success/', booking_success, name='booking_success'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
