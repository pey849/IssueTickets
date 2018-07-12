from django.db import models

# Create your models here.
# Models in python are a Class which represents a table in a database
# Each type of data we have (Tickets, Users, etc) is represented by its own models
# Each model maps to a single table in a datebase
# field types: https://docs.djangoproject.com/en/2.0/ref/models/fields/

class Tickets(models.Model):
    #no more than 100 characters for title
    title = models.CharField(max_length=100)
    issueDescription = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    #sender

    def __str__(self):
        return self.title
