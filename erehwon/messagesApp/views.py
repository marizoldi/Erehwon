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
@csrf_exempt
def api_send_message(request):
    User = get_user_model()
    sender_user = request.user
    print sender_user
    recipient=request.GET.get('recipient')
    if recipient is None:
        recipient=request.POST.get('recipient')
        if recipient is None:
            # have to get it from the body because Django request.POST only contains form data
            body = json.loads(request.body)
            recipient=body['recipient']
            print('recipient %s' % recipient)
            if recipient is None:
                print("recipient was none") 
                print request

    recipient_user=User.objects.get(username=recipient)
    print('sender')
    print(sender_user, recipient_user)
    # sender=request.GET.get('sender') # for demo purposes
    # sender_user=User.objects.get(username=sender) # for demo purposes
    message_to_send=max(request.GET.get('message'), request.POST.get('message'), body['message'] if 'message' in body else None)
    print pm_write(sender=sender_user, recipient=recipient_user, subject='', body=message_to_send)
    return HttpResponse('{"status": "Message sent"}')



@login_required
@csrf_exempt
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
        correspondents.append({"name":User.objects.get(id=cid).username})
        
    return JsonResponse(list(correspondents), safe=False)
    

@login_required
@csrf_exempt
def api_get_conversation(request):
    """
    get messages
    """
    this_user = request.user
    users_from_body = json.loads(request.body) if request.body != '' else None
    users = max(request.GET.get('users'), request.POST.get('users'), users_from_body)
    if users is None:
        return JsonResponse({"error":"No users supplied"})

    if type(users) != list and type(users) != dict:
        users = users.split('|')
    else:
        users = users['users']

    User = get_user_model()
    conversations_requested = {}
    for correspondent in users:
        correspondent_user = User.objects.get(username=correspondent)
        conversations=Message.objects.filter((Q(recipient=this_user) & Q(sender=correspondent_user)) | (Q(recipient=correspondent_user) & Q(sender=this_user))).order_by('-id')[:15][::-1]
        
        fields = {'sender': 'fr',
                  'recipient': 'to',
                  'body': 'msg',
                  'sent_at': 'dt'}
        # conversations = [{field: getattr(conv, field) for field in fields} for conv in conversations]
        conversation = []
        for conv in conversations:
            this_conv = {}
            for field in fields:
                value=getattr(conv,field)
                if field in ['sender','recipient']:
                    value=value.username
                json_field_name = fields[field]
                this_conv[json_field_name]=value
            conversation.append(this_conv)
        conversations_requested[correspondent] = conversation
    return JsonResponse(conversations_requested, safe=False)


@login_required
def MessagesWidgetView(request):
    mw_template = django.template.loader.get_template("messages_widget.html")
    context = {"messages": ["asdf","asfefef","gaweg"]}
    return HttpResponse(mw_template.render(context, request))
