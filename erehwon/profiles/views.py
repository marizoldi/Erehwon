from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import logging

from registration.backends.hmac import views as registration_views

from profiles.models import Project, Idea, Message, CallForAction
from profiles.forms import ProjectForm

log = logging.getLogger("erehwon")


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

    return redirect('/', permanent=True)
    #return HttpResponseRedirect("/")


@login_required
def project_list(request):

	projects = Project.objects.filter(user=request.user)
	context = {'projects': projects}

	return render(request, 'profiles/my-projects.html', context)


@login_required
def project_update(request, project_id):

    project = get_object_or_404(Project, pk=project_id)
    # if project.user != request.user:
    #     return HttpResponseForbidden()

    project_update_form = ProjectForm(initial={'title':project.title, 'label':project.label, 'synopsis':project.synopsis})

    if request.method == 'POST':
        project_update_form = ProjectForm(request.POST, instance=request.project)
        if project_update_form.is_valid():
            project_details = project_update_form.save(commit=False)
            project_details.save(update_fields=['title', 'label', 'synopsis', 'material', 'is_added_to_map'])
            project_update_form.save_m2m()
            return redirect('/projects')
    else:
        project_update_form = ProjectForm()

    context = {'project_update_form': project_update_form}

    return render(request, 'profiles/project.html', context)


@login_required
def project_add(request):

    if request.method == 'POST':
        new_project_form = ProjectForm(request.POST, instance=request.user)
        log.info('Form saved')
        if new_project_form.is_valid():
            new_project_form.save(commit=False)
            new_project_form.user = request.user
            new_project_form.save()

            return redirect('/projects')
    else:
        new_project_form = ProjectForm()

    context = {'new_project_form': new_project_form}

    return render(request, 'profiles/project.html', context)


@login_required
def idea_list(request):

	ideas = Idea.objects.filter(user=request.user)
	context = {'ideas': ideas}

	return render(request, 'profiles/ideas.html', context)

@login_required
def call_list(request):

    calls = CallForAction.filter(user=request.user)
    context = {'calls': calls}

    return render(request, 'profiles/callforaction.html', context)
