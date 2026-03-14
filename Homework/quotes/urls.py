from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_tag/', views.add_tag, name='add_tag'),
    path('add_quote/', views.add_quote, name='add_quote')
]