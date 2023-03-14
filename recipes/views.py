from django.shortcuts import render
from django.http import HttpResponse
from recipes.forms import RecipeForm, UserForm, UserProfileForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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


@login_required
def create_recipe(request):
    form = RecipeForm(request.POST)

    if form.is_valid():
        user_recipe = request.user
        recipe_form = form.save(commit=False)
        recipe_form.User = user_recipe
        form.save()
        return redirect('recipes/my_account.html')
    
    else:
        print(form.errors)
    
    return render(request, 'recipes/create_recipe.html',  {'form': form})

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            
            profile.save()
            
            registered = True
        
        else:
            print("there has been an error registering: ")
            print(user_form.errors, profile_form.errors)
    
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    
    return render(request, 'recipes/register.html', context = {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return render(request, 'recipes/login.html')
        
        else:
            return HttpResponse("Unable to login.")
    
    else:
        return render(request, 'recipes/login.html')

@login_required
def logout_user(request):
    logout(request)
    return render(request, 'recipes/home.html')
