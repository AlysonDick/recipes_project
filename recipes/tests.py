from django.test import TestCase, Client
from recipes.models import UserProfile, Category, Recipe, User
from django.db import IntegrityError
from django.urls import reverse

class ModelsTests(TestCase):
    def test_DefaultPostsIs0(self):
        print("Test 1")
        userProfile = UserProfile()
        self.assertEqual(userProfile.number_of_posts==0, True)
    
    def test_DefaultRatingIs0(self):
        print("Test 2")
        userProfile=UserProfile()
        self.assertEqual(userProfile.rating==0, True)
    
    def test_CategoryNameIsUnique(self):
        print("Test 3")
        success=False
        category1 = Category(category_name="Muerto")
        category2 = Category(category_name="Muerto")
        try:
            category1.save()
            category2.save()
        except IntegrityError:
            success=True
        self.assertTrue(success)
    
    def test_CategoryNameMaxLengthIs30(self):
        success=False
        print("Test 4")
        try:
            category = Category(category_name="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",)
            category.full_clean(exclude=None, validate_unique=True, validate_constraints=True)
            category.save()
        except Exception as e:
            print(e)
            success=True
        self.assertTrue(success)

class ViewsTests(TestCase):
    def test_HomePageContextExists(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'Whatever is in boldmessage in home views.py')


    def test_RedirectCreateRecipeWithoutLoggingIn(self):
        response=self.client.get(reverse('recipes:create_recipe'))
        self.assertEqual(response.status_code,302)
    
    def test_CanCreateRecipeWhenLoggedIn(self):
        #HOW TO FORCE LOGIN?
        testUser=User.objects.get_or_create(username="test")
        response=self.client.get(reverse('recipes:create_recipe'))
        response.client.force_login(testUser, backend=None)
        print(response.url)
        self.assertEqual(response.status_code,200)


        


        





