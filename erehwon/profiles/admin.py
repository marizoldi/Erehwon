from django.contrib import admin

from custom_user.admin import EmailUserAdmin

# Register your models here.
from .models import ErehwonUser, Project, Idea, Message, CallForAction

class ErehwonUserAdmin(EmailUserAdmin):
    """
    You can customize the interface of your model here.
    """
    pass

admin.site.register(Project)
admin.site.register(Idea)
admin.site.register(Message)
admin.site.register(CallForAction)
admin.site.register(ErehwonUser, ErehwonUserAdmin)
