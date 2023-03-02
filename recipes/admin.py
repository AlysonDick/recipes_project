from django.contrib import admin
from recipes.models import User, Category, Recipe, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_ID', 'category_name')

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_ID', 'username', 'number_of_posts', 'rating')

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'recipe_ID', 'recipe_name', 'like_count', 'recipe_description')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'comment_ID', 'comment_date', 'comment_description')

admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comment, CommentAdmin)