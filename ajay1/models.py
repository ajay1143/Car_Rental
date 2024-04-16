from django.db import models

# Create your models here.

class Contact_Us(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contact = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name

class CarUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    car_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='car_images/')

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"



class Booking(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    car_model = models.CharField(max_length=100)
    pickup_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return self.fullname

