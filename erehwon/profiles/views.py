from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import logging
from registration.signals import user_registered

from registration.backends.hmac import views as registration_views

from profiles.models import Project, Idea, CallForAction
from profiles.forms import ProjectForm
from profiles.forms import IdeaForm

log = logging.getLogger("erehwon")



def logout_view(request):
    logout(request)

    return redirect('/', permanent=True)


@login_required
def user_page(request):

    return render(request, 'profiles/my-projects.html')


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
            project_details.save(update_fields=['title', 'synopsis', 'is_added_to_map'])
            project_update_form.save_m2m()
            return redirect('/projects')
    else:
        project_update_form = ProjectForm()

    context = {'project_update_form': project_update_form}

    return render(request, 'profiles/project.html', context)


@login_required
def project_add(request):

    if request.method == 'POST':
        new_project_form = ProjectForm(request.POST)
        if new_project_form.is_valid():
            new_project_form.save()
            return HttpResponseRedirect(reverse('user_page'))

    else:
        new_project_form = ProjectForm()

    context = {'new_project_form': new_project_form}

    return render(request, 'profiles/project.html', context)


@login_required
def idea_add(request):

    if request.method == 'POST':
        new_idea_form = IdeaForm(request.POST)
        if new_idea_form.is_valid():
            new_idea_form.save()
            return HttpResponseRedirect(reverse('user_page'))

    else:
        new_idea_form = IdeaForm()

    context = {'new_idea_form': new_idea_form}

    return render(request, 'profiles/add-ideas.html', context)


@login_required
def idea_list(request):

	ideas = Idea.objects.filter(user=request.user)
	context = {'ideas': ideas}

	return render(request, 'profiles/ideas.html', context)

@login_required
def call_list(request):

    calls = CallForAction.objects.filter(user=request.user)
    context = {'calls': calls}

    return render(request, 'profiles/callforaction.html', context)
