from django.http import HttpResponse
from django.shortcuts import render

from .models import Question
from django.template import loader
from .models import RegData

def index1(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:2]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context ={
        'latest_question_list':latest_question_list,
    }
    return HttpResponse(template.render(context,request))

def read_all_record(request):
    all_reg_records = RegData.objects.all()[0:]
    template = loader.get_template('polls/basetab.html')
    context ={
        'all_reg_records':all_reg_records,
    }
    return HttpResponse(template.render(context,request))

def jaiswal(request):
    return  HttpResponse("Hi this is jaiswal here welcome to django world")

def detail(request,question_id):
    return HttpResponse("You ara looking at question %s. " %question_id)

def results(request,question_id):
    response = "You are looking at the results of the question %s."
    return HttpResponse(response % question_id)

def tarun_deatils(request):
    return render(request,'polls/tarun.html')


def vote(request,question_id):
    return HttpResponse("You are voting on the question %s " %question_id)

def send_data(request):
    p = RegData(name_text ='tarun', gender_type='M',occupation_type='Enginner')
    p1 = RegData(name_text ='ravi', gender_type='M',occupation_type='Enginner')
    p2 = RegData(name_text ='gantiya', gender_type='M',occupation_type='Enginner')
    p3= RegData(name_text ='jonhes', gender_type='F',occupation_type='Enginner')
    reg_list =[p,p1,p2,p3]
    RegData.objects.bulk_create(reg_list)
    count = 1
    for reg_each in reg_list:
        print("reg_each ")
        reg_each.save()
        count+=1
    return HttpResponse("created record %d" %count)
