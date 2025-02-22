from django.contrib import admin
from .models import UserProfile , FarmerProfile ,ServiceOffered ,Equipment,EquipmentRequest

admin.site.register(UserProfile)
admin.site.register(FarmerProfile)
admin.site.register(ServiceOffered)
admin.site.register(Equipment)
admin.site.register(EquipmentRequest)