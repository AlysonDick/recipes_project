from django.urls import path
from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('my_account/', views.my_account, name = 'my account'),
    path('recipes/', views.recipes, name = 'recipes'),
    path('faq/', views.faq, name = 'faq'),
    path('about/', views.about, name = 'about'),
]