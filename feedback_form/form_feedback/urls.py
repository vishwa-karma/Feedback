from django.contrib import admin
from django.urls import path
from form_feedback import views

#from .views import homeView, #successView

urlpatterns = [
    #path('', views.homeView, name='feedbackhome'),
    path('', views.successView, name='submit_form'),
]