from django.shortcuts import render
from django.http import HttpResponse
from recipes.forms import RecipeForm, UserForm, UserProfileForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from recipes.bing_search import run_query
from django.urls import reverse


def home(request):
    result_list=[]
    context_dict = {'boldmessage' : 'Whatever is in boldmessage in home views.py'}
    #Search bar stuff
    if request.method=='POST':
        query=request.POST['query'].strip()
        if query:
            result_list=run_query(query)
            return redirect(reverse('recipes:search',kwargs={'result_list':result_list}))
    return render(request, 'recipes/home.html', context=context_dict)

def my_account(request): #pass url parameter for slug:
    #UserProfile = UserProfile.objects.filter(url=url_parameter)
    #User = UserProfile[0].user()
    #Recipes = Recipes.objects.filter(user=User)
    #returns a list of recipes that you can put inside the context dictionary
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

def search(request, result_list):
    context_dict={'result_list':result_list}
    return render(request, 'recipes/search.html', context=context_dict)

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
            if user.is_active:
                login(request, user)
                return render(request, 'recipes/my_account.html')
        
        else:
            return HttpResponse("Unable to login.")
    
    else:
        return render(request, 'recipes/login.html')

@login_required
def logout_user(request):
    logout(request)
    return render(request, 'recipes/home.html')

@login_required
def create_recipe(request):
    form = RecipeForm()
    
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            #user_recipe = request.user
            recipe_form = form.save(commit=False)
            recipe_form.User = request.user
            form.save()
            return redirect('recipes/my_account.html')
        else:
            print(form.errors)
    
    else:
        print(form.errors)
    
    return render(request, 'recipes/create_recipe.html',  {'form': form})

