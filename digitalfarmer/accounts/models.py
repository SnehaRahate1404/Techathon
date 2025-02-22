from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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
    
class FarmerProfile(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    land_size = models.DecimalField(max_digits=10, decimal_places=2)  # In acres
    crop_type = models.CharField(max_length=255)
    experience_years = models.IntegerField()

    def __str__(self):
        return f"{self.user.name} - Farmer"

class Equipment(models.Model):
    farmer = models.ForeignKey(FarmerProfile,on_delete=models.CASCADE , related_name="equipments")
    Equipment_name = models.CharField(max_length=225)
    description = models.TextField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.Equipment_name} -{self.farmer.user.name}"
    
    def get_contact_number(self):
        return self.farmer.user.phone
    
    def get_location(self):
        return self.farmer.user.location
    
class ServiceOffered(models.Model):
    equipment = models.ForeignKey(Equipment,on_delete=models.CASCADE,related_name="services")
    service_name = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return f"{self.service_name} by {self.equipment.Equipment_name} - {self.equipment.farmer.user.name}"
class EquipmentRequest(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='requests')
    requester_name = models.CharField(max_length=255)
    requester_phone = models.CharField(max_length=15)
    requester_location = models.CharField(max_length=255)
    requested_date = models.DateField()
    confirmed = models.BooleanField(default=False)
    confirmation_time = models.TimeField(null=True, blank=True)
    
    def is_available(self):
        # Check if the equipment is already booked for the requested date
        conflicting_requests = EquipmentRequest.objects.filter(
            equipment=self.equipment,
            requested_date=self.requested_date,
            confirmed=True
        )
        return conflicting_requests.count() == 0

    def __str__(self):
        return f"Request for {self.equipment.Equipment_name} by {self.requester_name} on {self.requested_date}"
   