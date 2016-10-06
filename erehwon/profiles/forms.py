from django import forms
from profiles.models import Project

from registration.forms import RegistrationForm

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title','synopsis')
