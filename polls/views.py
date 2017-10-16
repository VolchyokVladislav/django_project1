from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import RequestContext, loader


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))

def detail(request, question_id):
    return HttpResponse('You are locking to the question %s' % question_id)

def results(request, question_id):
    response = 'You are locking to the result question %s'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('You are voting to the question %s' % question_id)


# Create your views here.
