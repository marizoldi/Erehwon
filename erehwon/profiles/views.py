from django.shortcuts import render
from django.views.generic import TemplateView
from profiles.models import Message

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
