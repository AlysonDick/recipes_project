from django.urls import path
from recipes import views
from recipes.views import search



app_name = 'recipes'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('my_account/', views.my_account, name = 'my_account'),
    path('recipes/', views.recipes, name = 'recipes'),
    path('faq/', views.faq, name = 'faq'),
    path('about/', views.about, name = 'about'),
    path('create_recipe/', views.create_recipe, name = 'create_recipe'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('search/', views.search, name='search',),
    path("do_praise", views.do_praise, name="do_praise"),
    path('recipes/<slug:recipe_name_slug>/', views.show_recipe, name='show_recipe'),
    path('view_my_recipes/',views.view_recipes, name='view_my_recipes'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]