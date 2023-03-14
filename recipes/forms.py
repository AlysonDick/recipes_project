from django import forms
from recipes.models import UserProfile, Recipe
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
    category = forms.CharField(max_length=30, help_text="Recipe Category")
    recipe_name = forms.CharField(max_length=30, help_text="Recipe Name")
    recipe_description = forms.CharField(max_length=2000, help_text="Recipe Description")
    like_count = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    recipe_id = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Recipe
        fields = ('category', 'recipe_name', 'recipe_description')
