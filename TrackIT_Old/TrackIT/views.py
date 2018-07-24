#functions that will be fired when user visits certain URLs

from django.http import HttpResponse
from django.shortcuts import render

#function fire the function when visits the about page
def about(request):
    #return HttpResponse('about-me');
    # returned a rendered template
    return render(request, 'about.html')

def homepage(request):
    #return HttpResponse('homepage');
    return render(request, 'homepage.html')
