from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('', views.index, name="index" ),
    path("About", views.About, name="About"),
    path("Contact", views.Contact, name="Contact"),
    path("Services", views.Services, name="Services")
    
]
