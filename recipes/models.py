from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_description = models.CharField(max_length=500, default='') 
    number_of_posts = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username 

class Category(models.Model):
    category_name = models.CharField(max_length=30, unique = True)

    class Meta:
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.category_name
    
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='uploaded_by')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null = True)
    recipe_name = models.CharField(max_length=30, unique = True)
    like_count = models.IntegerField(default=0)
    recipe_ingredients = models.CharField(max_length=2000, default='') 
    recipe_steps = models.CharField(max_length=2000, default='') 
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.recipe_name)
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.recipe_name 


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    comment_date = models.DateField()
    comment_description = models.CharField(max_length=100)

    def __str__(self):
        return self.comment_description

class Praise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.user) + "-"+ str(self.recipe)

class SearchQuery(models.Model):
    query = models.CharField(max_length=100)
    time = models.DateTimeField()

    def __str__(self):
        return self.query
