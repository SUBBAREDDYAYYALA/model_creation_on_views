from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def topic(request):
    to = input('enter topic name : ')
    tob = Topic.objects.get_or_create(Topic_name = to )[0]
    tob.save()

    return HttpResponse('data inserted....')

def webpage(request):
    to = input('enter topic name : ')
    tob = Topic.objects.get_or_create(Topic_name = to )[0]
    tob.save()

    na = input('enter name : ')
    u = input('enter url : ')
    wob = Webpage.objects.get_or_create(Topic_name = tob, name = na ,url = u)[0]
    wob.save()

    return HttpResponse('data inserted....')


def accessrecords(request):

    to = input('enter topic name : ')
    tob = Topic.objects.get_or_create(Topic_name = to )[0]
    tob.save()

    na = input('enter name : ')
    u = input('enter url : ')
    wob = Webpage.objects.get_or_create(Topic_name = tob, name = na ,url = u)[0]
    wob.save()

    
    d=input('enter date : ')
    a=input('enter auther name : ')
    e=input('enter email : ')
    AO = Accessrecords.objects.get_or_create(name = wob,date=d,auth=a,email = e)


    return HttpResponse('data inserted....')


