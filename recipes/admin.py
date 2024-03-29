from django.contrib import admin
from recipes.models import UserProfile, Category, Recipe, Comment, SearchQuery
from django.contrib.auth.models import User

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)

class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('recipe_name',)}
    list_display = ('user', 'category', 'recipe_name', 'like_count', 'recipe_ingredients', 'recipe_steps', 'slug')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'comment_date', 'comment_description')


admin.site.register(UserProfile)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(SearchQuery)