from django.shortcuts import render
from django.views.generic import TemplateView


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

class ProjectsView(TemplateView):
    """
    The Dashboard project view.
    """

    template_name = "profiles/projects.html"

class DashboardView(TemplateView):
    """
    The Dashboard view as soon as user logs in.
    """

    template_name = "profiles/dashboard-logged-in.html"
