from django.db import models


#From ER diagram, attributes are: userID, username, password, NumOfPosts, Picture, Rating
class User(models.Model):
    user_ID = models.CharField(max_length=30, unique = True)
    username = models.CharField(max_length=30, unique = True)

    #^-- Do we want both a user_ID and username? How do we set up a user_ID?

    #password = models.CharField(max_length=15)  -- not sure if password goes here. Inlcuded until clarified
    number_of_posts = models.IntegerField(default=0)
    rating = models.IntegerField()   #Do we want a default for this?

    def __str__(self):
        return self.username #or self.user_ID


class Category(models.Model):
    category_ID = models.CharField(max_length=30, unique = True)
    category_name = models.CharField(max_length=30, unique = True)
    #^-- both ID and name?

    class Meta:
        verbose_name_plural = 'Categories'

        
    def __str__(self):
        return self.category_ID

#From ER diagram, attributes are: name, likecount, picture, description, foreign key to UserID and foreign key to CatID

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)



    recipe_ID = models.CharField(max_length=30, unique = True)
    recipe_name = models.CharField(max_length=30, unique = True)
    #^-- as with above, do we want to have both ID and name

    like_count = models.IntegerField(default=0)
    recipe_description = models.CharField(max_length=2000) #increased to 2000 characters?


    def __str__(self):
        return self.recipe_name 

#Foreign key to userID and recipeID
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    comment_ID = models.CharField(max_length=30, unique = True)
    comment_date = models.DateField()
    comment_description = models.CharField(max_length=100)

    def __str__(self):
        return self.comment_ID
