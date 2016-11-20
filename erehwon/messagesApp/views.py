from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

#from allauth.account.views import SignupView, LoginView

# Create your views here.

class MessagesProfileView(TemplateView):
    """
    The Profile view.
    """
    template_name = "messages_profile.html"


class MessagesIndexView(TemplateView):
    """
    The index view.
    """
    template_name = "messages_index.html"


@csrf_exempt
def logout(request):
    logout()
    render(request)
    return HttpResponseRedirect('/accounts/login')
