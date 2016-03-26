from django.conf.urls import patterns, url

from news import views

urlpatterns = patterns('',
    url(r'^$', views.popnews),
    url(r'^star/(\d+)/$', views.star),
    url(r'^news/(\d+)/$', views.news),
    url(r'^popnews/', views.popnews),
    url(r'^newnews/$', views.newnews),

)
