from django.urls import path
from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('my_account/', views.my_account, name = 'my account'),
]