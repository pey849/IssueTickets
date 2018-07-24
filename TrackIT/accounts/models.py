from django.db import models
#import our database of users that were eitehr create in the admin page or through our signup page
from django.contrib.auth.models import User

# Create your models here.
#create Account User roles. Are they a client, agent or both
class AccountUser(models.Model):
    trackITUserName = models.ForeignKey(User,on_delete=models.DO_NOTHING,default=None)
    isTrackITAgent = models.BooleanField(default=False)
    isTrackITClient = models.BooleanField(default=False)

    def __str__(self):
        return str(self.trackITUserName)
