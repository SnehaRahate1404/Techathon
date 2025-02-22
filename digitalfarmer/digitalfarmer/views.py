from django.shortcuts import render, redirect
# from django.contrib import messages

def home_page(request):
    return render(request, 'home.html')