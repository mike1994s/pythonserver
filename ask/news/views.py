#from django.shortcuts import render
from django.http import HttpResponse 
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from qa.models import Question, Answer
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_GET, require_POST

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout

from django.http import Http404

from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponseNotFound
from qa.forms import AskForm, AnswerForm, LoginForm, SignupForm
from news.forms import StarForm
from news.models import Star, News
from django.http import HttpResponseRedirect
from xml.dom.minidom import *
import urllib2
import requests
import urllib
import json
import HTMLParser
from bs4 import BeautifulSoup
from django_feedparser.settings import *
import feedparser
import pprint
from urllib import urlopen
from pprint import pprint
def getPage(starName):
    url="http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q="+starName
    r = requests.get(url)
    h = HTMLParser.HTMLParser()
    return BeautifulSoup(h.unescape(r.text)).text
def cron(request):
	stars= Star.objects.all()
  #  resString = "1) ";
	for star in stars:
		f = { 'q' : star.name, 'hl' : "ru", 'output' : 'rss'}
		params = urllib.urlencode(f)
		d = feedparser.parse('https://news.google.com/news?'+params)
		for field in d['entries']:
			news = News()
			news.header = field.title
			news.text =  field.title
			news.url = field.title_detail.base
			news.star = star
			news.save()
		#	print field.title
	return HttpResponse("ok")
  #  stars= Star.objects.all()
  #  resString = "1) ";
  #  for star in stars:
  #      res = json.loads(getPage(star.name))
#	for item in res['responseData']['results']:
#		news = News()
#		news.header =BeautifulSoup(item['title']).text
#		news.text = BeautifulSoup(item['content']).text
#		news.url = BeautifulSoup(item['url']).text
#		news.star = star
#		news.save()
	return HttpResponse("OK")

from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
def user_logout(request):
    logout(request)
    return redirect('/')
@require_POST
@login_required
def answer(request):
	if request.method == "POST":
		form  = AnswerForm(request.POST)
		form._user = request.user
		if form.is_valid():
			ans = form.save()
			url = ans.get_url()
			return HttpResponseRedirect(url)
	return HttpResponseRedirect("/")


@login_required
def addstar(request):
	if request.method == "POST":
		form = StarForm(request.POST)
		if form.is_valid():
			post = form.save()
			print post
			url = post.get_url()
			print url
			return HttpResponseRedirect(url)
	else:
			form = StarForm()
	return render(request, 'news/form.html', {
		'form': form
})

def star(request, *args, **kwargs):
    try:
        key = int(args[0])
        print key
      #  question=Question.objects.get(pk=key)
	star = Star.objects.get(pk=key)
	newses = News.objects.filter(star_id=key)
       # ans = Answer.objects.filter(question_id=key)        
       # form = AnswerForm(initial={'question':key})
    except ValueError, Question.DoesNotExist:
        return HttpResponseNotFound('<h1>No Page Here</h1>') 
 
    return render(request, 'news/star.html', {
       'star':star,
       'newses':newses
    })
def news(request, *args, **kwargs):
    try:
        key = int(args[0])
        print key
      #  question=Question.objects.get(pk=key)
  	print question
       # ans = Answer.objects.filter(question_id=key)        
       # form = AnswerForm(initial={'question':key})
    except ValueError, Question.DoesNotExist:
        return HttpResponseNotFound('<h1>No Page Here</h1>') 
 
    return HttpResponse("Ok ")
 
#    return render(request, 'qa/one_question.html', {
 #       'q':question,
  #       'a':ans,
   #      'form':form,
   # })
def popnews(request):
    return HttpResponse("Ok")
def newnews(request):
    return HttpResponse("Ok")

def page(request):
    numPage = request.GET.get('page')
    questions= Star.objects.all()
    page, paginator = paginate(request, questions)
    print page  
  #  return HttpResponse(numPage)
    return render(request, 'news/page.html', {
        'stars': page.object_list,
        'paginator':paginator,
        'page' : page,   
   })

def paginate(request, qs):
    try:
         limit = int(request.GET.get('limit', 10))
    except ValueError:
         limit = 10
    if limit > 100:
         limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
       raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page, paginator

def popular(request):
    qs= Question.objects
    qs = qs.order_by('rating')
    qs = qs.reverse()
    qs = qs.all();
    page, paginator = paginate(request, qs)
    return render(request, 'qa/question_by_author.html', {
        'questions': page.object_list,
        'paginator':paginator,
        'page' : page,
   })

def index(request):
   # path = 'angular/index.html'
    path = 'react/index.html'
    template = loader.get_template(path)
    context = Context();
    return HttpResponse(template.render(context))
# Create your views here.
