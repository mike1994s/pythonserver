
from rest_framework import serializers
from rest_framework import routers, serializers, viewsets
from django.conf.urls import url, include
from  news.models import News, Star
class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = ('name')

class NewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Star
        field = ('header', 'text', 'url')
class StarViewSet(viewsets.ModelViewSet):
    queryset = Star.objects.all()
    serializer_class = NewsSerializer
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


