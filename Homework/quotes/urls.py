from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('tag/<str:tag_name>/', views.tag_search, name='tag'),
    path('register/', views.register, name='register'),
    path('add/', views.add_quote, name='add_quote'),
]