from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
	# is_admin = models.BooleanField('Is admin', default=False)
	is_rider = models.BooleanField('Is rider', default=False)
	is_driver = models.BooleanField('Is driver', default=False)


class Riders(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=20, null=True)
	email = models.EmailField(max_length=200, null=True)
	password1 = models.CharField(max_length=20, null=True)
	password2 = models.CharField(max_length=20, null=True)


	def __str__(self):
		return self.name


class Measurement(models.Model):
    location = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Distance from {self.location} to {self.destination} is {self.distance} km"


