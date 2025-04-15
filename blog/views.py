from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer
# Create your views here.

bot=ChatBot( 'chatbot',read_only=False,
            logic_adapters=[
                {
                    'import_path':'chatterbot.logic.BestMatch',
                    # 'default_response':'sorry dont know',
                    # 'maximum_similarity_threshold':0.90

                 
                 
                 
                 }
                 ])

list_of_trainer=[
      

       # Personal Questions
    "What is your name?",
    "I am a chatbot created to assist you.",
    "How are you?",
    "I am just a program, but I'm functioning as expected!",
    "What can you do?",
    "I can chat with you and help answer your questions.",

    # Small Talk
    "Tell me a joke",
    "Why don't scientists trust atoms? Because they make up everything!",
    "Tell me another joke",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What is your favorite color?",
    "I don't have preferences, but I think blue is calming.",

    # Assistance
    "Can you help me?",
    "Of course! What do you need help with?",
    "I need assistance",
    "Sure, let me know how I can assist you.",

    # Farewell
      "Goodbye",
    "Goodbye! Have a great day!",
    "See you later",
    "Take care! See you soon!",
    "Bye",
    "Bye! Have a nice day!",

    # Random Questions
    "What is the capital of France?",
    "The capital of France is Paris.",
    "What is 2 + 2?",
    "2 + 2 equals 4.",
    "Who is the president of the United States?",
    "It depends on the current year. Please check the latest news.",

    # Encouragement
    "I feel sad",
      "I'm sorry to hear that. Remember, tough times don't last forever.",
    "I am stressed",
    "Take a deep breath. Everything will be okay.",
    "I am happy",
    "That's great to hear! Keep smiling!",

    # Fun Facts
    "Tell me a fun fact",
    "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible!",
    "Tell me another fun fact",
    "Octopuses have three hearts. Two pump blood to the gills, and one pumps it to the rest of the body."
  

]
chatterBotCorpusTrainer=ChatterBotCorpusTrainer(bot)

# list_train=ListTrainer(bot)
# list_train.train(list_of_trainer)


chatterBotCorpusTrainer.train("chatterbot.corpus.english")

def index(request):
    return render(request,"blog/index.html")

def specific(request):
    return HttpResponse('this is specific')

# def getResponse(request):
#     userMessage=request.GET.get('userMessage')
#     chatResponse=str(bot.get_response(userMessage))
#     return HttpResponse(chatResponse)
def getResponse(request):
    userMessage = request.GET.get('userMessage')  
    if not userMessage:
        return HttpResponse("Please provide a valid message.")  
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)  