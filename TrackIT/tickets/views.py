from django.shortcuts import render, redirect
from .models import Tickets
from django.http import HttpResponse
#import the function to have login required to access a page when calling a function
from django.contrib.auth.decorators import login_required
#import the myForms.py file
from . import myForms

# Create your views here.

def ticket_list(request):
    #grabs all objects from the database of Tickets
    #order by the date field we set in models.py
    # send it to the view as a dictionary called myTickets
    tickets_to_give = Tickets.objects.all().order_by('date')
    return render(request, 'tickets/ticket_list.html', {'myTickets':tickets_to_give})

def ticket_details_views(request, slug):
    #return HttpResponse(slug)

    #query our database for a certain field we are looking for and place the object
    #we found from our query into a veriable
    #Ticket.object.get(field_tobase_search_on = varaible_passed_in)
    single_ticket = Tickets.objects.get(slug=slug)
    return render(request, 'tickets/ticket_details.html', {'single_ticket_details':single_ticket})

#login is required and if not logged in, do not execute the function
#instead redirect to the login page or the path you want to redirect to
@login_required(login_url="/accounts/login/")
def ticket_create_ticket_views(request):
    if request.method == 'POST':
        #retrieve the form's data. it validating the data we request from the post request
        #against the model form (CreateTicketForm) and we need the request.FILES the POST
        #does not include file uploads
        myTicketCreationForm = myForms.CreateTicketForm(request.POST, request.FILES)
        #check if form is valid
        if myTicketCreationForm.is_valid():
            #save article to database
            #get the instance of the form that was submitted, but tell it not to save just yet
            #this returns us an instance, so instance of the ticket that is going to be submitted
            createTicketInstance = myTicketCreationForm.save(commit=False)
            #now the request object knows who is logged in. we want to store it into the
            #reporter field in the createTicketInstance object which has a reporter field
            createTicketInstance.reporter = request.user
            #now we can save
            createTicketInstance.save()
            return redirect('ticket_app:list')
    else:
        #create a new instace of our model form and send it to the browser
        myTicketCreationForm = myForms.CreateTicketForm
    return render(request,'tickets/create_ticket.html', {'ticketForm':myTicketCreationForm})

#resolve the ticket. Basically we'll hide it from the list
def ticket_resolved_ticket_views(request, slug):
    instance = Tickets.objects.get(slug=slug)
    instance.resolved = True
    instance.save()
    print("resolved status: " + str(instance.resolved))
    return redirect('ticket_app:list')

#deleting an ticket from the database based on the slug found in the database
#potential problem if there is two tickets with the same slug
#should authenticate whether they are agents or clients
def ticket_delete_ticket_views(request, slug):
    instance = Tickets.objects.filter(slug=slug)
    instance.delete()
    return redirect('ticket_app:list')
