#import this idea of forms so we can create our own model forms
from django import forms
# we need access to our Ticket model from model.py
from . import models

#create a new model form which inherits from forms
#similar to UserCreationForm and AuthenticationForm
#we are just creating our own
class CreateTicketForm(forms.ModelForm):
    #create anotehr class to display which fields we want
    #in our form and which model did we want to inherit these fields from
    #which is from the Tickets model in model.py
    class Meta:
        model = models.Tickets
        #don't need to have date as it is automatically added upon creation
        #variable has to be called 'fields'
        fields = ['title', 'issueDescription', 'slug', 'attachment']
