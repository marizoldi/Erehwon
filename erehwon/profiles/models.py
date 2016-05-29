from django.db import models

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
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=30)
    synopsis = models.TextField(max_length=300)
    material = models.URLField(max_length=300, blank=True)
    contributors = models.CharField(max_length=20)
    active_status = models.BooleanField(default=1)
    label = models.CharField(max_length=30,
       choices=LABEL_OPTIONS, 
       default='A')

    def __str__(self):
        return self.title

