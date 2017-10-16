from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import RequestContext, loader
from django.template.response import TemplateResponse


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return TemplateResponse(request, 'polls/index.html', {
        'latest_question_list': latest_question_list,
    })

def detail(request, question_id):
    return HttpResponse('You are locking to the question %s' % question_id)

def results(request, question_id):
    response = 'You are locking to the result question %s'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('You are voting to the question %s' % question_id)


# Create your views here.
