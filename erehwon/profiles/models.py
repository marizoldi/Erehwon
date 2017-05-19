from django.db import models
from django.utils import timezone

from custom_user.models import AbstractEmailUser


class ErehwonUser(AbstractEmailUser):
#
#     # basic information
      username = models.CharField(max_length=30, blank=True)
#     #image (tip:s3DirectField)

def __str__(self):
        return self.username

class Project(models.Model):

   user = models.ForeignKey(ErehwonUser)
   title = models.CharField(max_length=30)
   synopsis = models.TextField(max_length=300)
   material = models.FileField(upload_to='MEDIA_ROOT')
   # contributors = models.CharField(max_length=20)
   active_status = models.BooleanField(default=1)
   is_added_to_map = models.BooleanField(default=0)

   def __str__(self):
       return self.title

class Idea(models.Model):

    # user = models.ForeignKey(ErehwonUser)
    project = models.ForeignKey('profiles.Project')
    title = models.CharField(max_length=30)
    synopsis = models.TextField(max_length=300)
    # contributors = models.CharField(max_length=20)


    def __str__(self):
        return self.title

class Message(models.Model):

   message = models.TextField(max_length=300)

   def __str__(self):
       return self.message

class CallForAction(models.Model):

    # user = models.ForeignKey(ErehwonUser)
    title = models.CharField(max_length=30)
    synopsis = models.TextField(max_length=300, default='Synopsis')
    action_location = models.CharField(max_length=30, default='Erehwon')
    date = models.DateTimeField(db_index=True, default=timezone.now)
    contributors = models.CharField(max_length=20, default='Erehwon')


    def __str__(self):
        return self.title
