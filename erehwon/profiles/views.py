from django.shortcuts import render
from django.views.generic import TemplateView

from profiles.models import Project

# Create your views here.
class LoginView(TemplateView):
    """
    The Login view.
    """

    template_name = "profiles/login.html"

class RegistrationView(TemplateView):
    """
    The Login view.
    """

    template_name = "profiles/register.html"


def project_list(request):

	projects = Project.objects.all()
	context = {'projects': projects}


	return render(request, 'profiles/my-projects.html', context)




class DashboardView(TemplateView):
    """
    The Dashboard view as soon as user logs in.
    """

    template_name = "profiles/dashboard-logged-in.html"

class IdeasView(TemplateView):
    """
    The Dashboard view to add ideas.
    """

    template_name = "profiles/ideas.html"

class CallForActionView(TemplateView):
    """
    The Dashboard view to create call for actions.
    """

    template_name = "profiles/callforaction.html"
