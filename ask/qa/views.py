#from django.shortcuts import render
from django.http import HttpResponse 
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from qa.models import Question, Answer
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET

from django.http import Http404
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
def test(request, *args, **kwargs):
    return HttpResponse('OK')
def question(request, *args, **kwargs):
    try:
        key = int(args[0])
        print key
        question=Question.objects.get(pk=key)        
    except ValueError, Question.DoesNotExist:
        return HttpResponseNotFound('<h1>No Page Here</h1>')  
    return render(request, 'qa/one_question.html', {
        'q':question,
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
