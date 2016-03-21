#from django.shortcuts import render
from django.http import HttpResponse 
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from qa.models import Question, Answer
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET, require_POST

from django.contrib.auth import authenticate, login

from django.http import Http404

from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponseNotFound
from qa.forms import AskForm, AnswerForm, LoginForm, SignupForm
from django.http import HttpResponseRedirect
def test(request, *args, **kwargs):
    return HttpResponse('OK')

from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
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

def dolog(request):
	user = request.user
	if user.is_authenticated():
		return HttpResponseRedirect("/")

	if request.method == "POST":
                form = LoginForm(request.POST)
                if form.is_valid():
			form.login(request)
                        return HttpResponseRedirect("/")
        else:
                        form = LoginForm()
        return render(request, 'qa/formlogin.html', {
                'form': form
})

def signup(request):
	user = request.user
        if user.is_authenticated():
                return HttpResponseRedirect("/")
	if request.method == "POST":
        	form = SignupForm(request.POST)
                if form.is_valid():
			new_user = form.save()
			form.login(new_user, request)
                        return HttpResponseRedirect("/")
        else:
                        form = SignupForm()
        return render(request, 'qa/formsignup.html', {
                'form': form
})

@login_required
def ask(request):
	if request.method == "POST":
		form = AskForm(request.POST)
		form._user = request.user
		if form.is_valid():
			post = form.save()
			print post
			url = post.get_url()
			print url
			return HttpResponseRedirect(url)
	else:
			form = AskForm()
	return render(request, 'qa/form.html', {
		'form': form
})

def question(request, *args, **kwargs):
    try:
        key = int(args[0])
        print key
        question=Question.objects.get(pk=key)
  	print question
        ans = Answer.objects.filter(question_id=key)        
        form = AnswerForm(initial={'question':key})
    except ValueError, Question.DoesNotExist:
        return HttpResponseNotFound('<h1>No Page Here</h1>') 
 
 
    return render(request, 'qa/one_question.html', {
        'q':question,
         'a':ans,
         'form':form,
    })
def page(request):
    numPage = request.GET.get('page')
    questions= Question.objects.all()
    page, paginator = paginate(request, questions)
    print page  
  #  return HttpResponse(numPage)
    return render(request, 'qa/question_by_author.html', {
        'questions': page.object_list,
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
    
    template = loader.get_template('qa/index.html')
    context = Context();
    return HttpResponse(template.render(context))
# Create your views here.
