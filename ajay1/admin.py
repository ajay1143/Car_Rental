from django.contrib import admin
from .models import Contact_Us, Car, CarUser

# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'contact', 'message']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', 'year', 'car_type', 'price']
    search_fields = ['brand', 'model', 'car_type']
    list_filter = ['brand', 'year', 'car_type']

@admin.register(CarUser)
class CarUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone']
    search_fields = ['username', 'email', 'phone']
