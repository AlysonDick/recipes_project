import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipes_project.settings')
django.setup()
from recipes.models import User, Recipe, Comment, Category

def populate():

    users = ['Alyson','James','Callum', 'Zihan', 'Liam', 'Temi','Wahab'
    ]

    categories = ['Easy', 'Healthy', 'Quick', 'Cheap']

    recipes = [{'category':categories[0]}]
    print(recipes)

    for user in users:
        u = add_user(user)  
        print(u)

    for category in categories:
        c = add_category(category)
        print(c)

def add_user(username):
    username = User.objects.get_or_create(username=username)[0]
    username.save()
    return username

def add_category(category_name):
    category = Category.objects.get_or_create(category_name=category_name)[0]
    category.save()
    return category

if __name__ == '__main__':
    populate()