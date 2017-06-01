from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import loader
import django.template
from django.db.models.query_utils import Q
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
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

def _send_message(request):
    ''' Send message between any requested recipient sender pair '''
    User = get_user_model()
    recipient=request.GET.get('recipient')
    sender=request.GET.get('sender')
    message_to_send=request.GET.get('body')
    recipient_user=User.objects.get(username=recipient)
    sender_user=User.objects.get(username=sender)
    print pm_write(sender=sender_user, recipient=recipient_user, subject='', body=message_to_send)
    return HttpResponse("Message sent")

@login_required
def api_send_message(request):
    User = get_user_model()
    sender_user = request.user
    print sender_user
    recipient=request.GET.get('recipient')
    if recipient is None:
        recipient=request.POST.get('recipient')
    print recipient
    recipient_user=User.objects.get(username=recipient)
    print('sender')
    print(sender_user, recipient_user)
    # sender=request.GET.get('sender') # for demo purposes
    # sender_user=User.objects.get(username=sender) # for demo purposes
    message_to_send=request.GET.get('message')
    print pm_write(sender=sender_user, recipient=recipient_user, subject='', body=message_to_send)
    return HttpResponse('{"status": "Message sent"}')



@login_required
def api_get_correspondents(request):
    # Retrieve list of correspondents
    user_id = request.user.id
    rv_convs = Message.objects.order_by('recipient_id','sender_id','id').filter(Q(recipient_id=user_id) | Q(sender_id=user_id)).values('recipient_id','sender_id').distinct('recipient_id','sender_id')[:500] # strange query but order by leftmost fields must match distinct, could be performance problems down the line..
    convs = rv_convs[::-1]
    correspondent_ids = set()
    for c in convs:
        correspondent_ids.add( c['recipient_id'])
    correspondent_ids.remove(user_id)

    # Convert user ids into usernames
    correspondents = []
    User = get_user_model()
    for cid in correspondent_ids:
        correspondents.append(User.objects.get(id=cid).username)
        
    return JsonResponse(list(correspondents), safe=False)
    
''' for demo purposes 
@login_required
def api_get_conversation(request):
    """
    get messages
    """
    recipient=request.GET.get('recipient')
    sender=request.GET.get('sender')
    #get a specific user e.g. sender with: 
    # from django.contrib.auth import get_user_model
    User = get_user_model()
    recipient_user = User.objects.get(username=recipient)
    sender_user = User.objects.get(username=sender)
    #json_output = Message.objects.all().filter(etc ).toJSON
    # from django.db.models.query_utils import Q
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
    '''

@login_required
def api_get_conversation(request):
    """
    get messages
    """
    user = request.user
    correspondent = request.GET.get('correspondent')
    if correspondent is None:
        correspondent = request.POST.get('correspondent')

    User = get_user_model()
    correspondent_user = User.objects.get(username=correspondent)
    conversations=Message.objects.filter((Q(recipient=user) & Q(sender=correspondent_user)) | (Q(recipient=correspondent_user) & Q(sender=user)))
    
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
    return JsonResponse(conversation_list, safe=False)

@login_required
def TestMessagesView(request):
    """
    Test Message API functionality
    """
    mv_template = django.template.loader.get_template("test_messages.html")
    context = {"messages": ["asdf","asfefef","gaweg"]}
    return HttpResponse(mv_template.render(context, request))

