"""erehwon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from core.views import HomepageView

from profiles.views import logout_view, LoginView, UserRegistrationView, RegistrationCompleteView, ActivationCompleteView, CallForActionView, ProjectFormView, message_list, project_list, idea_list, call_list
# from profiles.forms import ErehwonUserSignUpForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomepageView.as_view(), name="index"),
    url(r'^login', LoginView.as_view(), name="login"),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^accounts/logout', logout_view, name="logout_view"),
    url(r'^accounts/register', UserRegistrationView.as_view(), name="register"),
    url(r'^accounts/registration-complete/', RegistrationCompleteView.as_view(), name='registration_complete'),
    url(r'^accounts/activate/complete/', ActivationCompleteView.as_view(), name='activation_complete'),
    url(r'^projects', ProjectFormView.as_view(), name="project_form"),
    # url(r'^dashboard', message_list, name="dashboard"),
    url(r'^ideas', idea_list, name="idea_list"),
    url(r'^callforaction', call_list, name="call_list")

]
