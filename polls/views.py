from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("汝好。汝佇看問卷「%s」个細節。" % question_id)

def results(request, question_id):
    response = "汝好。汝佇看問卷「%s」个結果。"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("汝好。汝愛佇問卷「%s」投票。" % question_id)
