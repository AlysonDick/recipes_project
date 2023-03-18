import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipes_project.settings')
django.setup()
from recipes.models import User, Recipe, Comment, Category

def populate():

    users = ['Alyson','James','Callum', 'Zihan', 'Liam', 'Temi','Wahab'
    ]

    categories = ['Easy', 'Healthy', 'Quick', 'Cheap']

    recipes = [{'user':users[0], 'category':categories[0], 'recipe name': 'Fancy Pot Noodle', 'recipe ingredients':'Pot Noodle, Hot Water, Chicken, Stock Cube, Vegetables of your choosing', 'recipe steps':'Boil kettle, Prepare your chosen vegetables by washing and chopping, Once kettle is boiled add the hot water to a measuring jug with some stock and mix, Add the stock mixture and chicken to the pot noodle, Enjoy!'},
               {'user':users[1], 'category':categories[1], 'recipe name': 'Chicken and rice', 'recipe ingredients':'Chicken, Rice', 'recipe steps':'Cook rice to packet instructions'}]

    for user in users:
        u = add_user(user)  

    for category in categories:
        c = add_category(category) 

    for recipe in recipes:
        r = add_recipe(User.objects.get_or_create(username=recipe['user'])[0], Category.objects.get_or_create(category_name=recipe['category'])[0], recipe['recipe name'], recipe['recipe ingredients'], recipe['recipe steps'],)


def add_user(username):
    username = User.objects.get_or_create(username=username)[0]
    username.save()
    return username

def add_category(category_name):
    category = Category.objects.get_or_create(category_name=category_name)[0]
    category.save()
    return category

def add_recipe(user, category, recipe_name, recipe_ingredients, recipe_steps, like_count=0):
    recipe = Recipe.objects.get_or_create(recipe_name=recipe_name, like_count=like_count, recipe_ingredients=recipe_ingredients, recipe_steps=recipe_steps)[0]
    recipe.category = category
    recipe.user = user
    recipe.save()
    return recipe

if __name__ == '__main__':
    populate()