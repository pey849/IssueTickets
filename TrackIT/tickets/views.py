from django.shortcuts import render
from .models import Tickets
from django.http import HttpResponse

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
