from django.urls import path, re_path
#import the view.py file from the same directory
from . import views

urlpatterns = [
    #lsit of url pages we are going to create
    # r = regular express
    # ^ = this has to be the start of the sting
    # $ = this has to be the end of the string

    #the home page of tickets
    path('', views.ticket_list),

    #define a named capturing group for the first parameter
    #reference: https://stackoverflow.com/questions/7988942/what-does-this-django-regex-mean-p
    #re_path is just path but can also handle regular expressions syntax
    #so the captureing group is named 'slug', but this can be called anything you want
    #'slug' will be passed in as the function as a parameter
    # \w = any kind of letter or number and underscore
    # - = include the hyphen
    # + = this can be any length
    re_path(r'^(?P<slug>[\w-]+)/$', views.ticket_details_views),
]
