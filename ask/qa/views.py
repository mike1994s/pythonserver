#from django.shortcuts import render
from django.http import HttpResponse 
from django.template import Context, loader
def test(request, *args, **kwargs):
    return HttpResponse('OK')
def index(request):
    template = loader.get_template('qa/index.html')
    context = Context();
    return HttpResponse(template.render(context))
# Create your views here.