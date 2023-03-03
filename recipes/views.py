from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context_dict = {'boldmessage' : 'Whatever is in boldmessage in home views.py'}
    return render(request, 'recipes/home.html', context=context_dict)

def my_account(request):
    context_dict = {'my_account_message' : 'Whatever is in my_account_message in my_account views.py'}
    return render(request, 'recipes/my_account.html', context=context_dict)

def recipes(request):
    context_dict = {'recipes_message' : 'Whatever is in recipes_message in my_account views.py'}
    return render(request, 'recipes/recipes.html', context=context_dict)

def faq(request):
    context_dict = {'faq_message' : 'Whatever is in faq_message in my_account views.py'}
    return render(request, 'recipes/faq.html', context=context_dict)

def about(request):
    context_dict = {'about_message' : 'Whatever is in about_message in my_account views.py'}
    return render(request, 'recipes/about.html', context=context_dict)