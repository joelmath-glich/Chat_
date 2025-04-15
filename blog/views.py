from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
# Create your views here.

bot=ChatBot( 'chatbot',read_only=False,logic_adapters=['chatterbot.logic.BestMatch'])

list_of_trainer=[
        "Hi",
    "Hello! How can I help you?",
    "What is your name?",
    "I am a chatbot created to assist you.",
    "How are you?",
    "I am just a program, but I'm functioning as expected!",
    "Goodbye",
    "Goodbye! Have a great day!"
  

]

list_train=ListTrainer(bot)
list_train.train(list_of_trainer)

def index(request):
    return render(request,"blog/index.html")

def specific(request):
    return HttpResponse('this is specific')

def getResponse(request):
    userMessage=request.GET.get('userMessage')
    return HttpResponse(userMessage)