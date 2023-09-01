from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'ecommerce/home.html')

def contactus(request):
    return render(request, 'ecommerce/contactus.html')

def aboutus(request):
    return render(request, 'ecommerce/aboutus.html')