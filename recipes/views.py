import json
from django.shortcuts import render
from django.http import HttpResponse
from recipes.forms import RecipeForm, User, UserProfile, UserForm, UserProfileForm, CommentForm, SearchQueryForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from recipes.bing_search import run_query
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from recipes.models import Recipe, Praise, Category


from recipes.models import Recipe, SearchQuery
import datetime

def home(request):
    context_dict = {'boldmessage' : 'Whatever is in boldmessage in home views.py'}
    #Search bar stuff
    search_form=SearchQueryForm(request.POST)
    if request.method=='POST':
        if search_form.is_valid():
            f = search_form.save(commit=False)
            f.time = datetime.now()
            f.user = request.user
            f.save(commit=True)
            return redirect('recipes:search')
    return render(request, 'recipes/home.html', context=context_dict)


def my_account(request): 
    if request.user.is_authenticated:
        user = request.user
        user_profile = UserProfile.objects.all()
        user_profile = UserProfile.objects.filter(user=user)
        context_dict = {'user_profile':user_profile}

    else:
        #return HttpResponse("You can only view the My Account page if you are signed in. Please register or log in to view this page.")
        return render(request, 'recipes/register.html',)
    
    return render(request, 'recipes/my_account.html', context=context_dict)


def recipes(request):
    context_dict = {'recipes_message' : 'Whatever is in recipes_message in my_account views.py'}
    return render(request, 'recipes/recipes.html', context=context_dict)

@csrf_exempt
def do_praise(request):
    try:
        user = request.user
        if user.is_authenticated is False:
            resp = {"status": "1", "data": "need login"}
            return HttpResponse(json.dumps(resp), content_type="application/json")

        datas = json.loads(request.body)
        print(datas)
        id = datas["id"]
        mtype = datas["mtype"]
        print(id)
        print(mtype)
        recipe = Recipe.objects.filter(id=id)
        print(recipe)
        if len(recipe) == 0:
            # r = Recipe()
            # ca = Category()
            # ca.category_name = "food"
            # ca.save()
            # r.user=user
            # r.category = ca
            # r.recipe_name = "recipe1"
            # r.save()
            # recipe = r
            resp = {"status": "2", "data": u"recipe had deleted"}
            return HttpResponse(json.dumps(resp), content_type="application/json")
        else:
            recipe = recipe[0]
        if mtype == 0:

            old = Praise.objects.filter(user=user, recipe=recipe)
            if len(old) > 0:
                resp = {"status": "1", "data": u"you had praise"}
                return HttpResponse(json.dumps(resp), content_type="application/json")
            pr = Praise()
            pr.user = user
            pr.recipe = recipe
            pr.save()

            recipe.like_count = recipe.like_count + 1
            recipe.save()
        else:
            old = Praise.objects.filter(user=user, recipe=recipe)
            if len(old) == 0:
                resp = {"status": "1", "data": u"no praise"}
                return HttpResponse(json.dumps(resp), content_type="application/json")
            for i in old:
                i.delete()
                i.recipe.like_count = i.recipe.like_count -1
                i.recipe.save()

        resp = {"status": "0", "data": u"success"}

        return HttpResponse(json.dumps(resp), content_type="application/json")
    except Exception as e:
        print(e)
        resp = {"status": "3", "data": u"出错了"}
        return HttpResponse(json.dumps(resp), content_type="application/json")

def faq(request):
    context_dict = {'faq_message' : 'Whatever is in faq_message in my_account views.py'}
    return render(request, 'recipes/faq.html', context=context_dict)

def about(request):
    context_dict = {'about_message' : 'Whatever is in about_message in my_account views.py'}
    return render(request, 'recipes/about.html', context=context_dict)

def search(request):
    sq=SearchQuery.models.filter(user=request.user).order_by('-time')
    sqitem=sq[0]
    validRecipes = []
    recipesList = Recipe.objects.all()
    for x in recipesList:
        if sqitem in x:
            validRecipes.append(x)
    context_dict= {'results':validRecipes}
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
                return redirect(reverse('recipes:my_account'))
        
        else:
            return HttpResponse("Unable to login.")
    
    else:
        return render(request, 'recipes/login.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect(reverse('recipes:home'))

@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            rp = form.save(commit=False)
            rp.user = request.user
            form.save()
            
            return redirect(reverse('recipes:my_account'))
        else:
            print(form.errors)
    
    else:
        form = RecipeForm()

    
    return render(request, 'recipes/create_recipe.html',  {'form': form})

def show_recipe(request, recipe_name_slug):
    context_dict={}
    recipe = Recipe.objects.get(slug=recipe_name_slug)
    context_dict['recipe'] = recipe

    return render(request, 'recipes/recipes_test.html', context=context_dict)

def view_recipes(request):
    user = request.user
    user_profile = UserProfile.objects.all()
    user_profile = UserProfile.objects.filter(user=user)
    recipe_list = Recipe.objects.filter(user_id=user.id)
    context_dict = {'recipe_list' : recipe_list, 'user_profile':user_profile}
    
    return render(request, 'recipes/view_my_recipes.html', context=context_dict)
    
def test(request):
    recipe_list = Recipe.objects.all()
    print(recipe_list)
    context_dict = {'recipe_list' : recipe_list}

    return render(request, 'recipes/test.html', context=context_dict)