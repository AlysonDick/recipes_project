from django import forms
from recipes.models import UserProfile, Recipe, Category, Comment
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

class RecipeForm(forms.ModelForm):
    user = forms.HiddenInput()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    recipe_name = forms.CharField(max_length=30, help_text="Recipe Name")
    recipe_ingrediants = forms.CharField(max_length=2000, help_text="Ingrediants")
    recipe_steps = forms.CharField(max_length=2000, help_text="Steps")
    #recipe_picture = forms.ImageField(help_text="Recipe Picture")

    class Meta:
        model = Recipe
        fields = ('category', 'recipe_name','recipe_ingrediants', 'recipe_steps',)# 'recipe_picture',)

class CommentForm(forms.ModelForm):
    user = forms.HiddenInput()
    recipe = forms.ModelChoiceField(queryset=Recipe.objects.all())
    comment_text = forms.CharField(max_length=500, help_text='Comment')

    class Meta:
        model = Comment
        fields = ('recipe', 'comment_description',)