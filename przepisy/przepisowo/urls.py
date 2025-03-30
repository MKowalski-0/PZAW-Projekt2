from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import home, recipe_list, recipe_detail

urlpatterns = [
    path('', home, name='home'),
    path('przepisowo/', recipe_list, name='recipe_list'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
    path('recipes/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
]
