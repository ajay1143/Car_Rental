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

