from django.contrib import admin

# Register your models here.
from .models import Project, Idea, Message

admin.site.register(Project)
admin.site.register(Idea)
admin.site.register(Message)
