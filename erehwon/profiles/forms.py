from django import forms
from profiles.models import Project
from profiles.models import ErehwonUser
from profiles.models import Idea

from django.db.models import ImageField

from registration.forms import RegistrationForm


class ErehwonUserSignUpForm(RegistrationForm):

    class Meta:
        model = ErehwonUser
        fields = ('email', 'password1', 'password2', 'username')


class ProjectForm(forms.ModelForm):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Project
        fields = ('user', 'title', 'synopsis', 'image' )


class IdeaForm(forms.ModelForm):

	class Meta:
		model = Idea
		fields = ('user', 'project', 'title', 'synopsis', 'contributors')
