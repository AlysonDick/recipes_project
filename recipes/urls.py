from django.urls import path
from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('my_account/', views.my_account, name = 'my account'),
]