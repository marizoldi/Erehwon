from django.shortcuts import render
from django.views.generic import TemplateView

from profiles.models import Project, Idea, Message


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

def idea_list(request):

	ideas = Idea.objects.all()
	context = {'ideas': ideas}


	return render(request, 'profiles/ideas.html', context)


class DashboardView(TemplateView):
    """
    The Dashboard view as soon as user logs in.
    """
    def get_daily_message(self):
        """Returns message list from DB"""
    	all_messages = Message.objects.all()
        random_msg = random.sample(items, 1)
        return random_msg

    template_name = "profiles/dashboard-logged-in.html"


class CallForActionView(TemplateView):
    """
    The Dashboard view to create call for actions.
    """

    template_name = "profiles/callforaction.html"

