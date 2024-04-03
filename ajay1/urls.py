from django.contrib import admin
from django.urls import path
from ajay1 import views

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
]
