from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    identity = models.CharField(max_length=50, choices=[
        ('Farmer', 'Farmer'),
        ('Labour', 'Labour'),
        ('Krushi Kendra', 'Krushi Kendra'),
        ('gov_clerk', 'Government Clerk'),
        ('Market_clerk', 'Market Clerk')
    ])
    location = models.CharField(max_length=255)
    password = models.CharField(max_length=255)  # Store hashed password

    def __str__(self):
        return self.name