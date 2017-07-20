from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.db.models import Q
from profiles.models import Project, ErehwonUser
from itertools import chain
import time

def index( request ):
    return render_to_response( 'index.html', {}, context_instance = RequestContext( request ) )

def ajax_search( request ):

    if request.is_ajax():
        q = request.GET.get( 'q' )
        u = request.GET.user
        if q is not None:  
            if request.user.is_authenticated:
                project_results = Project.objects.filter(
                    Q( title__contains = q ) |
                    Q( synopsis__contains = q ) |
                    Q( user__contains = q))
            else:
                project_results = Project.objects.filter(
                    Q( title__contains = q ) |
                    Q( synopsis__contains = q ) )

        context = {'project_results': project_results}

        return render( request, 'result_list.html', context )
