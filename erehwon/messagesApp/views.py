from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from postman.models import Message
from postman.api import pm_write

import json


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

def api_send_message(request):
    User = get_user_model()
    recipient=request.GET.get('recipient')
    sender=request.GET.get('sender')
    message_to_send=request.GET.get('body')
    recipient_user=User.objects.get(username=recipient)
    sender_user=User.objects.get(username=sender)
    print pm_write(sender=sender_user, recipient=recipient_user, subject='', body=message_to_send)
    return HttpResponse("Message sent")

@login_required
def api_get_conversation(request):
    """
    get messages
    """
    recipient=request.GET.get('recipient')
    sender=request.GET.get('sender')
    ''' get a specific user e.g. sender with: '''
    from django.contrib.auth import get_user_model
    User = get_user_model()
    recipient_user = User.objects.get(username=recipient)
    sender_user = User.objects.get(username=sender)
    #json_output = Message.objects.all().filter(etc ).toJSON
    from django.db.models.query_utils import Q
    conversations=Message.objects.filter((Q(recipient=recipient_user) & Q(sender=sender_user)) | (Q(recipient=sender_user) & Q(sender=recipient_user)))
    fields = ['sender','recipient','body']
    # conversations = [{field: getattr(conv, field) for field in fields} for conv in conversations]
    conversation_list = []
    for conv in conversations:
        this_conv = {}
        for field in fields:
            value=getattr(conv,field)
            if field in ['sender','recipient']:
                value=value.username
            this_conv[field]=value
        conversation_list.append(this_conv)
    json_output = json.dumps(conversation_list)
    return HttpResponse(json_output)
