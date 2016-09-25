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
from django.conf.urls import url
from django.contrib import admin

from core.views import HomepageView
from profiles.views import LoginView, RegistrationView, CallForActionView, project_update, message_list, project_list, idea_list, call_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomepageView.as_view(), name="index"),
    url(r'^login', LoginView.as_view(), name="login"),
    url(r'^register', RegistrationView.as_view(), name="register"),
    url(r'^projects', project_update, name="project_update"),
    url(r'^dashboard', message_list, name="dashboard"),
    url(r'^ideas', idea_list, name="idea_list"),
    url(r'^callforaction', call_list, name="call_list"),
]
