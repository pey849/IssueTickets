from django.urls import path, re_path
#import the view.py file from the same directory
from . import views

app_name = 'ticket_app'

urlpatterns = [
    #lsit of url pages we are going to create
    # r = regular express
    # ^ = this has to be the start of the sting
    # $ = this has to be the end of the string

    #the home page of tickets
    path('', views.ticket_list, name="list"),

    #urls should be above the one below so the regex doesn't get confused
    #that the path we are going to is part of a slug
    path('create/', views.ticket_create_ticket_views, name="create"),

    path('myTickets/', views.ticket_list, name="myAssignedTickets"),

    #path is ../slug/resolve/ which calls the resolve function and then redirects back to the list
    re_path(r'^(?P<slug>[\w-]+)/resolve/$', views.ticket_resolved_ticket_views, name="resolve"),

    #define a named capturing group for the first parameter
    #reference: https://stackoverflow.com/questions/7988942/what-does-this-django-regex-mean-p
    #re_path is just path but can also handle regular expressions syntax
    #so the captureing group is named 'slug', but this can be called anything you want
    #'slug' will be passed in as the function as a parameter
    # **the name you give it MUST match the parameter name you have setup in your views.py
    # so if you named it 'foo' the function 'ticket_details_views' must have a parameter named 'foo' as well
    # \w = any kind of letter or number and underscore
    # - = include the hyphen
    # + = this can be any length
    re_path(r'^(?P<slug>[\w-]+)/$', views.ticket_details_views, name="details"),
]
