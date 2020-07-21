from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("index")


def login(request):
    print("输出A安全等级的算法")
    return HttpResponse("login")

def safe_b(request):
    print("输出B安全等级算法")
    return HttpResponse("实现了安全等级为b的级别")

def safeA(request):
    return HttpResponse("实现了A级别的安全等级")


def reg(request):
    return HttpResponse("实现注册功能")

