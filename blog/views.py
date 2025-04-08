from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# Create your views here.


def index(request):
    return render(request,"blog/index.html")

def specific(request):
    return HttpResponse('this is specific')

def getResponse(request):
    