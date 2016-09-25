from django.db import models
from django.utils import timezone

LABEL_OPTIONS = (
    ('A','Activism'),
    ('DA','Digital Activism'),
    ('CD','Community Development'),
    ('UP','Urban Planning'),
    ('NE','New Ecologies'),
    ('AE','Alternative Economies'),
    ('CM','Citizen Movement'),
    ('AI','Artistic Interventions'),
)

class Project(models.Model):

   #user = models.ForeignKey('auth.User')
   title = models.CharField(max_length=30)
   synopsis = models.TextField(max_length=300)
   material = models.URLField(max_length=300, blank=True)
   # contributors = models.CharField(max_length=20)
   active_status = models.BooleanField(default=1)
   is_added_to_map = models.BooleanField(default=0)
   label = models.CharField(max_length=30,
       choices=LABEL_OPTIONS,
       default='A')

   def __str__(self):
       return self.title

class Idea(models.Model):

    user = models.ForeignKey('auth.User')
    project = models.ForeignKey('profiles.Project')
    title = models.CharField(max_length=30)
    synopsis = models.TextField(max_length=300)
    # contributors = models.CharField(max_length=20)
    label = models.CharField(max_length=30,
        choices=LABEL_OPTIONS,
        default='A')

    def __str__(self):
        return self.title

class Message(models.Model):

   message = models.TextField(max_length=300)

   def __str__(self):
       return self.message

class CallForAction(models.Model):

    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=30)
    synopsis = models.TextField(max_length=300, default='Synopsis')
    action_location = models.CharField(max_length=30, default='Erehwon')
    date = models.DateTimeField(db_index=True, default=timezone.now)
    contributors = models.CharField(max_length=20, default='Erehwon')
    call_label = models.CharField(max_length=30,
    choices=LABEL_OPTIONS,
    default='A')

    def __str__(self):
        return self.title
