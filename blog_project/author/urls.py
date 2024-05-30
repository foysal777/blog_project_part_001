
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('author/', views.add_author , name= 'add_author'),
 
]
