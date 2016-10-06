from django.contrib import admin

# Register your models here.
from .models import Project, Idea, Message, CallForAction, ErehwonUser

admin.site.register(Project)
admin.site.register(Idea)
admin.site.register(Message)
admin.site.register(CallForAction)
admin.site.register(ErehwonUser)
