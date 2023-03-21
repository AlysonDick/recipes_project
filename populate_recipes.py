import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipes_project.settings')
django.setup()
from recipes.models import User, Recipe, UserProfile, Category

def populate():

    users = [{'username':'Alyson', 'user_profile_description': "Hi, I'm Alyson. I'm not a very good cook and I'm trying to learn. I've got one recipe at the moment - hopefully I can make more soon."},
            {'username': 'James', 'user_profile_description':"Hi, I'm James. I like to cook in my spare time. Enjoy the recipes!"},
            {'username': 'Callum', 'user_profile_description':"Hi, I'm Callum. I like to cook in my spare time. Enjoy the recipes!"},
            {'username': 'Zihan', 'user_profile_description':"Hi, I'm Zihan. I like to cook in my spare time. Enjoy the recipes!"},
            {'username': 'Liam', 'user_profile_description':"Hi, I'm Liam. I like to cook in my spare time. Enjoy the recipes!"},
            {'username': 'Temi', 'user_profile_description':"Hi, I'm Temi. I like to cook in my spare time. Enjoy the recipes!"},
            {'username': 'Wahab', 'user_profile_description':"Hi, I'm Wahab. I like to cook in my spare time. Enjoy the recipes!"},
    ]

    categories = ['Easy', 'Healthy', 'Quick', 'Cheap']

    recipes = [{'user':users[0]['username'], 'category':categories[0], 'recipe name': 'Fancy Pot Noodle', 'recipe ingredients':'Pot Noodle, Hot Water, Chicken, Stock Cube, Vegetables of your choosing', 'recipe steps':'Boil kettle, Prepare your chosen vegetables by washing and chopping, Once kettle is boiled add the hot water to a measuring jug with some stock and mix, Add the stock mixture and chicken to the pot noodle, Enjoy!', 'like count':10},
               {'user':users[1]['username'], 'category':categories[1], 'recipe name': 'Chicken and rice', 'recipe ingredients':'The only ingredients you need are chicken and rice', 'recipe steps':'Cook rice to packet instructions', 'like count':5},
               {'user':users[2]['username'], 'category':categories[2], 'recipe name': 'Scrambled eggs', 'recipe ingredients': 'Eggs, Salt, Pepper, Milk, Oil', 'recipe steps': 'Crack three eggs in to a bowl and season with salt and pepper. Add milk to the eggs and whisk. Heat oil in a pan on a low-medium heat. Add eggs to pan and stir continuously until eggs are cooked.','like count':3},
               {'user':users[3]['username'], 'category':categories[3], 'recipe name': 'Beans on toast', 'recipe ingredients': 'Your favourite baked beans and bread', 'recipe steps': 'Heat up beans either in microwave or in a pan on the cooker. While your beans are heating, toast your bread. Plate as you like','like count':8},
               {'user':users[4]['username'], 'category':categories[0], 'recipe name': 'Creamy Pesto Pasta', 'recipe ingredients': 'Pasta of your choice - spaghetti works well! -, jarred pesto, single cream', 'recipe steps': 'Boil some water in a pan and cook to packet instructions. When cooked, drain your pasta and keep some of the pasta water. Add some pesto to the pan, along with three tbsp of your cream and stir. Add some pasta water. Serve.','like count':15},
               {'user':users[5]['username'], 'category':categories[1], 'recipe name': 'Vegetable Soup', 'recipe ingredients': 'Carrot, Leek, Lentils, Veg Stock, Potato, Onion', 'recipe steps': 'Dice carrot, potato and onion. Saute in a pan until soft. Cut leek in to slices. Add to the vegetable mix with lentil and vegetable stock. Bring the pan to a boil and simmer for 30 minutes or until lentils are cooked.','like count':7 },
               {'user':users[6]['username'], 'category':categories[2], 'recipe name': 'Pasta Aglio e Olio', 'recipe ingredients': 'Spaghetti, garlic, parsley, salt, pepper, chilli flakes, good quality olive oil', 'recipe steps': 'Boil water and add this to a pan with lots of salt. Finely slice garlic, and chop parsley. Heat olive oil in a pan. Add the garlic and cook for a couple of minutes. Then add chilli, salt and pepper. Remove from the heat before the garlic browns. Wehn cooked, remove pasta from the pan and place directly in to the pil and garlic mixture. Stir and add the parsley.','like count':6 },
               {'user':users[5]['username'], 'category':categories[3], 'recipe name': 'Baked potato with tuna mayo', 'recipe ingredients': 'One large potato, canned tuna and mayo', 'recipe steps': 'Prick potato all over with a fork and put in microwave for five minutes, or until starting to soften. Drain tuna and combine with mayo in a bowl. Once soft, put the potato in a preheated oven for around half an hour, until the skin is crispy. Remove from oven, slice in half down the middle and add the tuna mayo mixture.','like count':11},
               {'user':users[1]['username'], 'category':categories[0], 'recipe name': 'Chicken fajitas', 'recipe ingredients': 'Chicken breast, peppers, onion, wraps, chilli powder, paprika, cumin, garlic powder and ground coriander', 'recipe steps': 'Begin by chopping the veg and chicken to your liking. Add the chicken to a hot pan with some oil. Then add the seasonings. Once the chicken is cooked, remove from the pan and cook the veg in the same pan. Serve on a wrap.','like count':9},
               {'user':users[2]['username'], 'category':categories[1], 'recipe name': 'Sweet chili salmon and rice', 'recipe ingredients': 'Salmon, sweet chili sauce, rice', 'recipe steps': 'Bake the salmon in an oven until alomst cooked. Add chili sauce to salmon and put back in oven until fully cooked. Cook rice according to packet instructions','like count':4},
               {'user':users[3]['username'], 'category':categories[2], 'recipe name': 'Teriyaki salmon', 'recipe ingredients': 'Salmon and teriyaki sauce', 'recipe steps': 'Bake the salmon until almost cooked. Add sauce to salmon and place back in oven until fully cooked','like count': 1},
               {'user':users[4]['username'], 'category':categories[3], 'recipe name': 'Egg fried rice', 'recipe ingredients': 'Rice, eggs, soy sauce', 'recipe steps': 'Fry rice in a pan for a couple of minutes, crack egg directly in to pan and stir. Add soy sauce to taste','like count':14},
               {'user':users[5]['username'], 'category':categories[0], 'recipe name': 'Home made pizza', 'recipe ingredients': 'Flour, yeast, salt, passata, garlic, mozzarella and toppings of your choice', 'recipe steps':'To make the base, mix flour, yeast, salt and warm water in a bowl to form a dough. Knead for five minutes. Roll the dough to your desired shape and top with some passata, garlic and the toppings of your choice. Bake in an oven on the highest heat until golden.','like count':13 },
               {'user':users[6]['username'], 'category':categories[1], 'recipe name': 'Bean stew', 'recipe ingredients':'Onion, tinned tomatoes, garlic, canned mixed beans', 'recipe steps': 'Saute onion and garlic in a pan, add tinned tomatoes when cooked and allow to thicken. Then add mixed beans.','like count':2},
               {'user':users[1]['username'], 'category':categories[2], 'recipe name': 'Sweet chili chicken', 'recipe ingredients': 'Chicken, sweet chili sauce', 'recipe steps': 'Fry chicken in a pan. When cooked through, add some sweet chilli sauce','like count':12}]
    
    user_profile_description = ["Hi, I'm Alyson. I'm not a very good cook and I'm trying to learn. I've got one recipe at the moment - hopefully I can make more soon.",
                                "James here. I like to cook in my spare time. Enjoy the recipes!",
                                "Callum here. I like to cook in my spare time. Enjoy the recipes!",
                                "Zihan here. I like to cook in my spare time. Enjoy the recipes!",
                                "Liam here. I like to cook in my spare time. Enjoy the recipes!",
                                "Temi here. I like to cook in my spare time. Enjoy the recipes!",
                                "Wahab here. I like to cook in my spare time. Enjoy the recipes!",]
    for user in users:
        u = add_user(user)  
        u = add_description(user)

    for category in categories:
        c = add_category(category) 

    for recipe in recipes:
        r = add_recipe(User.objects.get_or_create(username=recipe['user'])[0], Category.objects.get_or_create(category_name=recipe['category'])[0], recipe['recipe name'], recipe['recipe ingredients'], recipe['recipe steps'], recipe['like count'],)


def add_user(user):
    username = User.objects.get_or_create(username=user['username'])[0]
    #print(username)
    username.save()
    user_prof_description = UserProfile.objects.get_or_create(user=username)[0]
    #user_prof_description = UserProfile.objects.values('profile_description')
    user_prof_description = UserProfile.objects.update(profile_description=user['user_profile_description'])
    #user_prof_description = UserProfile.objects.get_or_create(profile_description=user['user_profile_description'])
    #print(username)
    #print(user_prof_description, "PROFILE")
    #username.save()
    return username

def add_description(user):
    username = User.objects.get_or_create(username=user['username'])[0]
    description = user['user_profile_description']
    user_profile = UserProfile.objects.get_or_create(user=username)[0]
    user_profile.profile_description = description
    user_profile.save()
    return user_profile
    

def add_category(category_name):
    category = Category.objects.get_or_create(category_name=category_name)[0]
    category.save()
    return category

def add_recipe(user, category, recipe_name, recipe_ingredients, recipe_steps, like_count):
    recipe = Recipe.objects.get_or_create(recipe_name=recipe_name, like_count=like_count, recipe_ingredients=recipe_ingredients, recipe_steps=recipe_steps)[0]
    recipe.category = category
    recipe.user = user
    recipe.save()
    return recipe

if __name__ == '__main__':
    populate()