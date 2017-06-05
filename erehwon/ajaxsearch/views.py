from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.db.models import Q
from django.contrib.auth.models import Project, ErehwonUser
from itertools import chain
import time

def index( request ):
    return render_to_response( 'index.html', {}, context_instance = RequestContext( request ) )

def ajax_user_search( request ):

    if request.is_ajax():
        q = request.GET.get( 'q' )
        if q is not None:
            result_list = []
            project_results = Project.objects.filter(
                Q( title__contains = q ) |
                Q( synopsis__contains = q ) )
            user_results = ErehwonUser.objects.filter(username__contains = q)

            result_list = sorted(chain(project_results, user_results)

            return render_to_response( 'results.html', { 'result_list': result_list, },
                                       context_instance = RequestContext( request ) )
