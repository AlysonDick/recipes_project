from django import forms
from recipes.models import UserProfile, Recipe, Category, Comment
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    profile_description = forms.CharField(max_length=500, help_text="Profile description - tell us about yourself here.")
    class Meta:
        model = User
        fields = ('username', 'password', 'profile_description')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

class RecipeForm(forms.ModelForm):
    user = forms.HiddenInput()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    recipe_name = forms.CharField(max_length=30, help_text="Recipe Name")
    recipe_ingredients = forms.CharField(max_length=2000, help_text="Ingredients")
    recipe_steps = forms.CharField(max_length=2000, help_text="Steps")


    class Meta:
        model = Recipe
        fields = ('category', 'recipe_name','recipe_ingredients', 'recipe_steps',)

class CommentForm(forms.ModelForm):
    user = forms.HiddenInput()
    recipe = forms.ModelChoiceField(queryset=Recipe.objects.all())
    comment_text = forms.CharField(max_length=500, help_text='Comment')

    class Meta:
        model = Comment
        fields = ('recipe', 'comment_description',)