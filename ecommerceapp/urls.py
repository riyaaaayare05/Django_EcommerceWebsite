from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contact', views.contactus, name='contactus'),
    path('about', views.aboutus, name='aboutus'),
]