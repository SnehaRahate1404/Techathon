from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
import tensorflow as tf
import numpy as np
from PIL import Image
import os
# from tensorflow.keras import models
from django.conf import settings
# from .db_connection import insert
from django.db import connection
from .utility import get_translation
# from accounts.models import Equipment, ServiceOffered, FarmerProfile,UserProfile,EquipmentRequest

from django.contrib import messages


# Load your pre-trained model only once
# model_path = os.path.join(settings.BASE_DIR, 'train/train.keras')
# model = models.load_model(model_path)

# Mapping predicted class indices to actual labels
class_names = ['Potato___Early_Blight','Potato___Healthy', 'Potato___Late_Blight'] 

# def crop_disease(request):
#     prediction_result = None
#     if request.method == 'POST' and request.FILES['image']:
#         image_file = request.FILES['image']
#         image = Image.open(image_file)
#         image = image.resize((256, 256))  # Resize to match model input size
#         img_array = np.array(image) / 255.0  # Normalize
#         img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

#         predictions = model.predict(img_array)
#         predicted_class = class_names[np.argmax(predictions[0])]
#         confidence = round(100 * np.max(predictions[0]), 2)
#         prediction_result = f"{predicted_class} ({confidence}%)"

#     return render(request, 'crop_disease.html', {'prediction_result': prediction_result})

def homepage(request):
    # Get the selected language from the session, default to English
    lang = request.session.get('language', 'en')

    # Fetch translated text
    context = {
        'welcome_heading': get_translation('welcome_heading', lang),
        'welcome_heading_2': get_translation('welcome_heading_2', lang),
        'welcome_subheading': get_translation('welcome_subheading', lang),
        'register_button': get_translation('register_button', lang),
        'login_button': get_translation('login_button', lang),
        'about_us_heading': get_translation('about_us_heading', lang),
        'about_us_description': get_translation('about_us_description', lang),
        'know_more_button': get_translation('know_more_button', lang),
        'services_heading': get_translation('services_heading', lang),
        'farmer_service': get_translation('farmer_service', lang),
        'labour_service': get_translation('labour_service', lang),
        'government_scheme_service': get_translation('government_scheme_service', lang),
        'market_service': get_translation('market_service', lang),
        'video_tutorials_heading': get_translation('video_tutorials_heading', lang),
        'go_to_videos_button': get_translation('go_to_videos_button', lang),
    }
    # if 'user_id' not in request.session:
    #   return redirect('user_login')  # Redirect to login if not authenticated
    request.session.flush()
    return render(request, 'home.html', context )

def change_language(request, lang):
    request.session['language'] = lang
    return redirect(request.META.get('HTTP_REFERER', '/'))

def about_us(request):
    # Get the selected language from the session, default to English
    lang = request.session.get('language', 'en')

    # Fetch translated text
    context = {
        'welcome_heading': get_translation('welcome_heading', lang),
        'welcome_heading_2': get_translation('welcome_heading_2', lang),
        'welcome_subheading': get_translation('welcome_subheading', lang),
        'register_button': get_translation('register_button', lang),
        'login_button': get_translation('login_button', lang),
        'about_us_heading': get_translation('about_us_heading', lang),
        'about_us_description': get_translation('about_us_description', lang),
        'know_more_button': get_translation('know_more_button', lang),
        'services_heading': get_translation('services_heading', lang),
        'farmer_service': get_translation('farmer_service', lang),
        'labour_service': get_translation('labour_service', lang),
        'government_scheme_service': get_translation('government_scheme_service', lang),
        'market_service': get_translation('market_service', lang),
        'video_tutorials_heading': get_translation('video_tutorials_heading', lang),
        'go_to_videos_button': get_translation('go_to_videos_button', lang),
    }

    return render(request ,"about_us.html" ,context)

def contact_us(request):
    return render(request ,"contact-us.html")

def profile(request):
    # Assuming request.user is an instance of UserProfile.
    user_profile = request.user

    if request.method == "POST":
        # Get form values from POST data
        name = request.POST.get('name', user_profile.name)
        phone = request.POST.get('phone', user_profile.phone)
        email = request.POST.get('email', user_profile.email)
        # Optional: If you add alternate phone or gender to your model, capture them here.
        # For example:
        # alternate_phone = request.POST.get('alternate_phone', user_profile.alternate_phone)
        # gender = request.POST.get('gender', user_profile.gender)

        # Update the user_profile object
        user_profile.name = name
        user_profile.phone = phone
        user_profile.email = email
        # Update other fields if available...
        user_profile.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('profile')  # Replace 'profile' with your URL name

    context = {
        'user_profile': user_profile,
    }
    return render(request, 'profile.html', context)

def farmer_home(request):
    return render(request,"index.html")

def video_home(request):
    return render(request,"video_tut.html")

def  market_page(request):
    return render(request,"market.html")

def  labour_book(request):
    return render(request,"labour-book.html")

def  rent_equipment(request):
    return render(request,"rent-equipment-page.html")

def  explore_more(request):
    return render(request,"explore-more-equip.html")


