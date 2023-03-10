from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    number_of_posts = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username #or self.user_ID

class Category(models.Model):
    category_name = models.CharField(max_length=30, unique = True)

    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.category_name
    
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    recipe_name = models.CharField(max_length=30, unique = True)
    like_count = models.IntegerField(default=0)
    recipe_description = models.CharField(max_length=2000) 


    def __str__(self):
        return self.recipe_name 

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    comment_date = models.DateField()
    comment_description = models.CharField(max_length=100)

    def __str__(self):
        return self.comment_description

