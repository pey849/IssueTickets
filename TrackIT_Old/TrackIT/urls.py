"""TrackIT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#import the view.py file from the same directory
from . import views
#allows us to append to url patterns so django can handle the serving up static patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
#import the settings.py file
from django.conf import settings

#since we already importing views from the current directory above
#we need to give it an alias to tell which view we are referencing
#when we have more than one imported views
from tickets import views as ticket_views

urlpatterns = [
    #lsit of url pages we are going to create
    # r = regular express
    # ^ = this has to be the start of the sting
    # $ = this has to be the end of the string
    path('admin/', admin.site.urls),
    #about page
    path('about/', views.about),
    #the home page which is now being redirected to the ticket list page
    #in the urls.py in tickets folder and give it an alias of 'home'
    #when we just go to the base URL like no slug attached to it
    path('', ticket_views.ticket_list, name="home"),

    #include the urls from tickets
    path('tickets/', include('tickets.urls')),

    #include the urls from accounts
    path('accounts/', include('accounts.urls')),
]

# staticfiles_urlpatterns() functions checks if we are in debug mode
# if we are then it will append to urlpatterns so it will know how to
# serve up our static files
urlpatterns += staticfiles_urlpatterns()
#we have access to the variables in the settings.py file from the import above
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
