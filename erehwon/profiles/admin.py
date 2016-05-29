from django.contrib import admin

# Register your models here.
from .models import Project, Idea

admin.site.register(Project)
admin.site.register(Idea)
