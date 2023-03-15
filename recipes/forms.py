from django import forms
from recipes.models import UserProfile, Recipe, Category
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
    #user = forms.ModelChoiceField(forms.HiddenInput)
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    recipe_name = forms.CharField(max_length=30, help_text="Recipe Name")
    recipe_description = forms.CharField(max_length=2000, help_text="Recipe Description")

    class Meta:
        model = Recipe
        fields = ('category', 'recipe_name', 'recipe_description')
