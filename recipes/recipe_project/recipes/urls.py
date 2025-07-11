from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('create/', views.recipe_create, name='recipe_create'),
    path('update/<int:pk>/', views.recipe_update, name='recipe_update'),
    path('delete/<int:pk>/', views.recipe_delete, name='recipe_delete'),
]
