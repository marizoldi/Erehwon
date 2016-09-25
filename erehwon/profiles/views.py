from django.shortcuts import render
from django.views.generic import TemplateView

from profiles.models import Project, Idea, Message, CallForAction
from profiles.forms import ProjectForm


# Create your views here.
class LoginView(TemplateView):
    """
    The Login view.
    """

    template_name = "profiles/login.html"


class RegistrationView(TemplateView):
    """
    The Login view.
    """

    template_name = "profiles/register.html"


class CallForActionView(TemplateView):
    """
    The Dashboard view to create call for actions.
    """

    template_name = "profiles/callforaction.html"


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

    return render(request, 'profiles/project.html', context)


def project_list(request):

    projects = Project.objects.all()
    context = {'projects': projects}

    return render(request, 'profiles/my-projects.html', context)


def idea_list(request):

    ideas = Idea.objects.all()
    context = {'ideas': ideas}

    return render(request, 'profiles/ideas.html', context)


def message_list(request):

    message = Message.objects.all().order_by('?')[0]
    context = {'message': message}

    return render(request, 'profiles/dashboard-logged-in.html', context)


def call_list(request):

    calls = CallForAction.objects.all()
    context = {'calls': calls}

    return render(request, 'profiles/callforaction.html', context)
