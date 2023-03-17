from django.contrib import admin
from recipes.models import UserProfile, Category, Recipe, Comment
from django.contrib.auth.models import User

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'recipe_name', 'like_count', 'recipe_ingrediants', 'recipe_steps',)# 'recipe_picture',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'comment_date', 'comment_description')


admin.site.register(UserProfile)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comment, CommentAdmin)