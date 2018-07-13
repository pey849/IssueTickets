from django.shortcuts import render
from .models import Tickets

# Create your views here.

def ticket_list(request):
    #grabs all objects from the database of Tickets
    #order by the date field we set in models.py
    # send it to the view as a dictionary
    tickets = Tickets.objects.all().order_by('date')
    return render(request, 'tickets/ticket_list.html', {'tickets':tickets})
