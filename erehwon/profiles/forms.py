from django import forms

from profiles.models import Project

class ProjectForm(forms.ModelForm):

	class Meta:
		model = Project
		fields = ('title', 'label', 'synopsis', 'material', 'is_added_to_map')
