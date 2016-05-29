from django.db import models

class Project(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=30)
    synopsis = models.TextField(max_length=300)
    image = models.ImageField('Image', upload_to='path/', blank=True)
    material = models.URLField(max_length=300, blank=True)
    contributors = models.CharField(max_length=20)
    active_status = models.BooleanField(default=1)
    # ideas =

    def __str__(self):
        return self.title
