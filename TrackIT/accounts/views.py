from django.shortcuts import render
#import django's already defined form
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(request):
    #store django's prebuilt form in a variable
    myForm = UserCreationForm()
    #send to the signup.html page the variable 'accountForm'
    return render(request,'accounts/signup.html', {'accountForm':myForm})
