from django import forms
from profiles.models import Project

from profiles.models import ErehwonUser

from registration.forms import RegistrationForm


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title','label')

class ErehwonUserSignUpForm(RegistrationForm):

    class Meta:
        model = ErehwonUser
        fields = ('email', 'password1', 'password2', 'username')
