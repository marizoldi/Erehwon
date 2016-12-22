from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from custom_user.admin import EmailUserAdmin

# Register your models here.
from .models import ErehwonUser, Project, Idea, Message, CallForAction
from .forms import ErehwonUserSignUpForm

class ErehwonUserAdmin(EmailUserAdmin):
    """
    You can customize the interface of your model here.
    """

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('username',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'username')}
        ),
    )
    add_form = ErehwonUserSignUpForm
    list_display = ('email', 'username', 'is_staff')
    search_fields = ('email', 'username')
    ordering = ('email',)

    pass

admin.site.register(Project)
admin.site.register(Idea)
admin.site.register(Message)
admin.site.register(CallForAction)
admin.site.register(ErehwonUser, ErehwonUserAdmin)
