from django.urls import path
#import the view.py file from the same directory
from . import views

urlpatterns = [
    #lsit of url pages we are going to create
    # r = regular express
    # ^ = this has to be the start of the sting
    # $ = this has to be the end of the string

    #the home page of tickets
    path('', views.ticket_list)
]
