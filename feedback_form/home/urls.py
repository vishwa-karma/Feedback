from django.contrib import admin
from django.urls import path
from home import views

#from .views import homeView, #successView

urlpatterns = [
    path('', views.homeView, name='home'),
    #path('success/', successView, name='success'),
]