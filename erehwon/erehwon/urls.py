from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from core.views import HomepageView

from profiles.views import logout_view, CallForActionView, ProjectFormView, project_add, project_list, project_update, idea_list, call_list
from profiles.forms import ErehwonUserSignUpForm
from registration.backends.hmac.views import RegistrationView

from messagesApp.views import MessagesProfileView, MessagesIndexView
import notifications.urls

import postman.urls
from messagesApp.views import api_send_message,api_get_conversation

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/register/$', RegistrationView.as_view(form_class=ErehwonUserSignUpForm), name="registration_register"),
    url(r'^accounts/', include('registration.backends.hmac.urls')), # This line includes automatically all views and urls for registration/activation/password reset
    url(r'^$', HomepageView.as_view(), name="index"),
    #url(r'^accounts/logout/$', logout_view, name="logout_view"),
    # url(r'^dashboard', loggedin_view, name="dashboard"),
    url(r'^projects/$', project_list, name="project_list"),
    # url(r'^project', ProjectFormView.as_view(), name="project_form"),
    url(r'^ideas/$', idea_list, name="idea_list"),
    url(r'^callforaction/$', call_list, name="call_list"),

    # django-postman
    url(r'^messages/erehwon/$', MessagesIndexView.as_view(), name='MessagesIndex View'),
    url(r'^messages/messageprofile/$', MessagesProfileView.as_view(), name='MessagesProfile View'),

    #TODO write some custom postman views
    #css classes here: http://django-postman.readthedocs.io/en/latest/views.html
    #and hook them up.
    url(r'^inbox/$', TemplateView.as_view(template_name='inbox.html')),
    url(r'^messages/', include('postman.urls', namespace='postman', app_name='postman')),
    # django-notifications-hq
    url(r'^inbox/notifications/', include(notifications.urls, namespace='notifications')),
    url(r'^api/sendmessage/$', api_send_message, name='Api Send Message View'),
    url(r'^api/messages/$', api_get_conversation, name='API Get Messages'),
]
