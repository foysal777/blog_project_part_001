
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('add_profile/', views.profile , name= 'add_profiles'),
 
]
