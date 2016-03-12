from django.conf.urls import patterns, url

from qa import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^login/', views.test),
    url(r'^signup/', views.test),
    url(r'^question/(\d+)/$', views.test),
    url(r'^ask/$', views.test),
    url(r'^popular/', views.test),
    url(r'^new/$', views.test),

)
