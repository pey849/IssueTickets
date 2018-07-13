from django.db import models

# Create your models here.
# Models in python are a Class which represents a table in a database
# Each type of data we have (Tickets, Users, etc) is represented by its own models
# Each model maps to a single table in a datebase
# field types: https://docs.djangoproject.com/en/2.0/ref/models/fields/

# if you make any new vairables in the class, and have preexiting data, set a default
# then run the command "python manage.py makemigrations" and "python manage.py migrate"
# then start the server

class Tickets(models.Model):
    #no more than 100 characters for title
    title = models.CharField(max_length=100)
    issueDescription = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, default="")
    #sender

    def __str__(self):
        return self.title

    def ticketDescriptionSnippet(self):
        #take up to the 50th character
        return self.issueDescription[:50] + "..."
