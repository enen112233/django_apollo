from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("index")


def login(request):
    return HttpResponse("login")

def safe_b(request):
    return HttpResponse("实现了安全等级为b的级别")

def safeA(request):
    return HttpResponse("实现了A级别的安全等级")


