from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, UpdateView

from profiles.models import Project, Idea, Message, CallForAction
from profiles.forms import ProjectForm


# Create your views here.


class CallForActionView(TemplateView):
    """
    The Dashboard view to create call for actions.
    """

    template_name = "profiles/callforaction.html"

class ProjectFormView(TemplateView):
        """
        The Dashboard view for create/update Projects
        """

        template_name = "profiles/my-projects.html"
        form_class = ProjectForm


def project_list(request):

	projects = Project.objects.all()
	context = {'projects': projects}


	return render(request, 'profiles/my-projects.html', context)

def idea_list(request):

	ideas = Idea.objects.all()
	context = {'ideas': ideas}


	return render(request, 'profiles/ideas.html', context)


def message_list(request):

	message = Message.objects.all().order_by('?')[0]
	context = {'message': message}


	return render(request, 'profiles/dashboard-logged-in.html', context)


def call_list(request):

    calls = CallForAction.objects.all()
    context = {'calls': calls}


    return render(request, 'profiles/callforaction.html', context)
