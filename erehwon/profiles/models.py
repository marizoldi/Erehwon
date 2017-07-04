from django.db import models
from django.utils import timezone

from custom_user.models import AbstractEmailUser

class ErehwonUser(AbstractEmailUser):
#
#     # basic information
      username = models.CharField(max_length=30, blank=True)

def __str__(self):
        return self.username

class File(models.Model):
    filename = models.CharField(max_length=220)
    file = models.BinaryField()
    def __str__(self):
        return self.filename


from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible # deals with serialization error in Project
@deconstructible
class FlexStorage(Storage):
    def open(self, name, mode='rb'):
        f = File.objects.filter(filename=name)
        return f.read()
    def _save(self, name, content): 
        content.open() # reopen, file seek 0
        f = File(filename=name, file=content.file.read())
        f.save()
        return name
    def exists(self, name):
        f_list = File.objects.filter(filename=name)
        return len(f_list) > 0
    def delete():
        files = File.objects.filter(filename=name)
        for f in files:
            f.delete()
    # def listdir():
    # def size():
    # def url():


def get_storage():
    return FlexStorage()

class Project(models.Model):
    user = models.ForeignKey(ErehwonUser)
    title = models.CharField(max_length=30)
    synopsis = models.TextField(max_length=300)
    image = models.ImageField(storage=get_storage(), null=True, blank=True)

    files = models.ForeignKey(File, on_delete=models.CASCADE,
                                 null=True, blank=True)
    material = models.URLField(max_length=300, blank=True)
    contributors = models.CharField(max_length=20)
    active_status = models.BooleanField(default=1)
    is_added_to_map = models.BooleanField(default=0)
 
    def __str__(self):
        return self.title

class ProjectFile(models.Model):
    file = models.OneToOneField(File, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Idea(models.Model):

    user = models.ForeignKey(ErehwonUser)
    project = models.ForeignKey('profiles.Project')
    title = models.CharField(max_length=30)
    synopsis = models.TextField(max_length=300)
    contributors = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class CallForAction(models.Model):

    user = models.ForeignKey(ErehwonUser)
    title = models.CharField(max_length=30)
    synopsis = models.TextField(max_length=300, default='Synopsis')
    action_location = models.CharField(max_length=30, default='Erehwon')
    date = models.DateTimeField(db_index=True, default=timezone.now)
    contributors = models.CharField(max_length=20, default='Erehwon')

    def __str__(self):
        return self.title
