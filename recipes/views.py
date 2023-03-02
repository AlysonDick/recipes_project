from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context_dict = {'boldmessage' : 'Whatever is in boldmessage in home views.py'}
    return render(request, 'recipes/home.html', context=context_dict)

def my_account(request):
    context_dict = {'my_account_message' : 'Whatever is in my_account_message in my_account views.py'}
    return render(request, 'recipes/my_account.html', context=context_dict)
