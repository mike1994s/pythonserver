from django.conf.urls import patterns, include, url
from rest_framework import routers, serializers, viewsets

from  news.models import News, Star
from django.contrib import admin
admin.autodiscover()




class NewsSerializer(serializers.ModelSerializer):
#    star =serializers.Field(source='star.name',ReadOnlyField)
   # star = StarSerializer() 
  
    class Meta:
        model = News
        fields = ('header', 'text', 'url')
class StarSerializer(serializers.ModelSerializer):
    newses =NewsSerializer(source='news_set', many=True)
       
    class Meta:
        model = Star
        fields = ('name','rating', 'newses')

class StarViewSet(viewsets.ModelViewSet):
    queryset = Star.objects.all()
    serializer_class = StarSerializer
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'stars', StarViewSet)
router.register(r'newnews', NewsViewSet)
urlpatterns = patterns('',
    # Examples:
    url(r'^api/', include(router.urls)),
#    url(r'^$', 'news.views.index'),
    url(r'^$', 'news.views.page'),
    url(r'^pages/', 'news.views.page'),
    url(r'^popular/$', 'qa.views.popular'), 
    url(r'^login/', 'qa.views.dolog'),
    url(r'^signup/', 'qa.views.signup'),
    url(r'^question/(\d+)/$', 'qa.views.question'),
    url(r'^ask/$', 'qa.views.ask'),
    url(r'^new/$', 'qa.views.test'), 
    url(r'^answer/$', 'qa.views.answer'), 
    url(r'^logout/$', 'qa.views.user_logout'),  
    url(r'^news/', include('news.urls')),  
    url(r'^star/(\d+)/$', 'news.views.star'),
    url(r'^news/(\d+)/$', 'news.views.news'),
    url(r'^popnews/', 'news.views.popnews'),
    url(r'^newnews/$', 'news.views.newnews'),
    url(r'^cron/$', 'news.views.cron'), 
    url(r'^addstar/$', 'news.views.addstar'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
