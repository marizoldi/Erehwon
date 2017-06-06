from django.conf.urls import *
from ajaxsearch.views import *

urlpatterns = [
         url( r'^$', index, name = 'test_index' ),
         url( r'^home/search/$', ajax_search, name = 'test_search' ),
         ]
