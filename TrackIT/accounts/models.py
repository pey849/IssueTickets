from django.db import models
#import our database of users that were eitehr create in the admin page or through our signup page
from django.contrib.auth.models import User
from roles.models import Roles

# Create your models here.
#create Account User roles. Are they a client, agent or both
class AccountUser(models.Model):
    trackITUserName = models.ForeignKey(User,on_delete=models.DO_NOTHING,default=None)
    #Foreign key to point to different roles a user can be
    trackITRoleType = models.ForeignKey(Roles,on_delete=models.DO_NOTHING,default=None, null=True, blank=True)

    def __str__(self):
        return str(self.trackITUserName)
