from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from core.views import HomepageView

from profiles.views import logout_view, project_add, user_page, project_update, idea_list, call_list, search
from profiles.forms import ErehwonUserSignUpForm
from registration.backends.hmac.views import RegistrationView

from messagesApp.views import MessagesProfileView, MessagesIndexView, MessagesWidgetView
import notifications.urls

import postman.urls
from messagesApp.views import api_send_message, api_get_conversation, api_get_correspondents

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/register/$', RegistrationView.as_view(form_class=ErehwonUserSignUpForm), name="registration_register"),
    url(r'^accounts/', include('registration.backends.hmac.urls')), # This line includes automatically all views and urls for registration/activation/password reset
    url(r'^accounts/login$', auth_views.login, name='login'),
    url(r'^$', HomepageView.as_view(), name="index"),
    url(r'^accounts/logout/$', logout_view, name="logout"), # {'next_page': 'homepage'}, name="logout"),
    url(r'^home/$', user_page, name="user_page"),
    url(r'^home/addproject/$', project_add, name="project_add"),
    url(r'^ideas/$', idea_list, name="idea_list"),
    url(r'^calls/$', call_list, name="call_list"),
    url(r'^search/$', search, name="search"),

    # django-postman
    url(r'^messages/erehwon/$', MessagesIndexView.as_view(), name='MessagesIndex View'),
    url(r'^messages/messageprofile/$', MessagesProfileView.as_view(), name='MessagesProfile View'),
    url(r'^messages/widget/$', MessagesWidgetView, name='Messages Widget View'),

    #TODO write some custom postman views
    #css classes here: http://django-postman.readthedocs.io/en/latest/views.html
    #and hook them up.
    url(r'^inbox/$', TemplateView.as_view(template_name='inbox.html')),
    url(r'^messages/', include('postman.urls', namespace='postman', app_name='postman')),
    # django-notifications-hq
    url(r'^inbox/notifications/', include(notifications.urls, namespace='notifications')),
    url(r'^api/sendmessage/$', api_send_message, name='Api Send Message View'),
    url(r'^api/get_conversation/$', api_get_conversation, name='Api Get Conversation View'),
    url(r'^api/messages/$', api_get_conversation, name='API Get Messages'),
    url(r'^api/correspondents/$', api_get_correspondents, name='API Get Correspondents'),
]
