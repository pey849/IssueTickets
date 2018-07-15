from django.shortcuts import render, redirect
#import django's already defined form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#import django's built in login function
from django.contrib.auth import login

# Create your views here.
def signup_view(request):
    #if the request is a POST request
    if request.method == 'POST':
        #take the data from the form's POST request and validate it
        # basically check if the data is ok, does the user exists already,
        # is the password ok, is the password too short, etc
        myForm = UserCreationForm(request.POST)
        #check if form is valid
        if myForm.is_valid():
            #if valid, save the form's data to the database
            #this function also returns the user to us
            user = myForm.save()
            #log the user in after sign up
            login(request, user)
            #redirect the user to the list of ticket or whatever page you want
            #redirect to the urls.py file that the app_name is ticket_app
            #and the url link that is named 'list'
            return redirect('ticket_app:list')

    #else it probably a GET request
    else:
        #store django's prebuilt form in a variable
        myForm = UserCreationForm()

    #send to the signup.html page the variable 'accountForm'
    return render(request,'accounts/signup.html', {'accountForm':myForm})

def login_view(request):
    if request.method == 'POST':
        #we need to name the data as this is the actual first expected
        #parameter it expects
        myAuthForm = AuthenticationForm(data=request.POST)
        if myAuthForm.is_valid():
            # login the User
            #we can get the user from the Authentication Form; this is built into django
            user = myAuthForm.get_user()
            #the login function we imported from django
            #takes the requst object and the user that is logging in
            login(request,user)
            return redirect('ticket_app:list')
    #else its a post method
    else:
        myAuthForm = AuthenticationForm()

    return render(request, 'accounts/login.html', {'loginForm':myAuthForm})
