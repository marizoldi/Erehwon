from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from registration.backends.hmac import views as registration_views

from profiles.models import Project, Idea, Message, CallForAction
from profiles.forms import ProjectForm


# Create your views here.

class CallForActionView(TemplateView):
    """
    The Dashboard view to create call for actions.
    """

    template_name = "profiles/callforaction.html"

class ProjectFormView(TemplateView):
    """
    The Dashboard view for create/update Projects
    """

    template_name = "profiles/my-projects.html"
    form_class = ProjectForm

def logout_view(request):
    logout(request)

    return HttpResponseRedirect("/")

@login_required
def project_list(request):

	projects = Project.objects.all()
	context = {'projects': projects}


	return render(request, 'profiles/my-projects.html', context)

@login_required
def project_update(request):
    if request.method == 'POST':
        project_update_form = ProjectForm(request.POST)
        if project_update_form.is_valid():
            project_details = project_update_form.save(commit=False)
            project_details.save(update_fields=['title', 'label', 'synopsis', 'material', 'is_added_to_map'])
            return redirect('project_update')
    else:
        project_update_form = ProjectForm()

    context = {'project_update_form': project_update_form}

    return render(request, 'profiles/my-projects.html', context)


@login_required
def idea_list(request):

	ideas = Idea.objects.all()
	context = {'ideas': ideas}


	return render(request, 'profiles/ideas.html', context)

@login_required
def call_list(request):

    calls = CallForAction.objects.all()
    context = {'calls': calls}


    return render(request, 'profiles/callforaction.html', context)
