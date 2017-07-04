from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import logging
import magic
from registration.signals import user_registered

from registration.backends.hmac import views as registration_views

from profiles.models import Project, Idea, CallForAction, File, ProjectFile
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
            project_details.save(update_fields=['title', 'label', 'synopsis', 'is_added_to_map'])
            project_update_form.save_m2m()
            return redirect('/projects')
    else:
        project_update_form = ProjectForm()

    context = {'project_update_form': project_update_form}

    return render(request, 'profiles/project.html', context)

# Example how to access and display projects
def projects_list(request):
    projects = Project.objects.all()
    out = ''
    for project in projects:
        project_files = ProjectFile.objects.filter(project_id=project.id)
        project_files = [pf.file.filename for pf in project_files]
        project_file_links = ["<a href=\"/files/%s\"> %s </a>" % (pf, pf) for pf in project_files]
        out += """<div> 
                      Title: %s <br> 
                      Synopsis: %s <br> 
                      <img src=/imgsrv/%s>  
                      Files: %s <br>
                      ProjectFiles: %s <br>
                      ProjectFileLinks: %s <br>
                 </div> """ % (
               project.title, 
               project.synopsis, 
               project.image,
               project.files,
               project_files,
               project_file_links)
    return HttpResponse(out)

def serve_file(request, file_name):
    files = File.objects.filter(filename=file_name)
    if len(files) == 0:
        return HttpResponse("No such file/image")
    f = files[0]    
    if len(f.file) > 0:
        mime_type = magic.from_buffer(f.file[0:min(len(f.file),1024)])
        return HttpResponse(f.file, mime_type) # 'image/jpg')
serve_image = serve_file # different aliases for images and files

@login_required
def project_add(request):
    if request.method == 'POST':
        new_project_form = ProjectForm(request.POST, request.FILES)
        if new_project_form.is_valid():
            # Save Project Image
            if 'image' in request.FILES and request.FILES['image'].size > 0 and request.FILES['image'].size < 60 * 1000000:
                img = request.FILES['image'] # .read()
            else:
                img = None

            this_proj = new_project_form.save()
            files = request.FILES.getlist('file_field')
            for f in files:
                # First save file
                this_f = File(filename=f, file=f.read())
                this_f.save()
                # Then save project file relation
                pf = ProjectFile(project=this_proj, file=this_f)
                pf.save()
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
