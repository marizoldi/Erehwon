from django import forms
from profiles.models import Project

from profiles.models import ErehwonUser, Project

from registration.forms import RegistrationForm


class ProjectForm(forms.ModelForm):

	class Meta:
		model = Project
		fields = ('user', 'title', 'label', 'synopsis', 'material', 'is_added_to_map')

class ErehwonUserSignUpForm(RegistrationForm):

    class Meta:
        model = ErehwonUser
        fields = ('email', 'password1', 'password2', 'username')
