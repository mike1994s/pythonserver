from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'qa.views.page'),
    url(r'^popular/$', 'qa.views.popular'), 
    url(r'^login/', 'qa.views.test'),
    url(r'^signup/', 'qa.views.test'),
    url(r'^question/(\d+)/$', 'qa.views.question'),
    url(r'^ask/$', 'qa.views.ask'),
    url(r'^new/$', 'qa.views.test'), 
    url(r'^answer/$', 'qa.views.answer'), 
     
   # url(r'^test/$', include('qa.urls')),  
	
)
