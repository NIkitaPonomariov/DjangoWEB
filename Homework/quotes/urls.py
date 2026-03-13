from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('tag/<str:tag_name>/', views.tag_search, name='tag'),
    path('register/', views.register, name='register'),
    path('add/', views.add_quote, name='add_quote'),
    path('add_author/', views.add_author, name='add_author'),
    path('accounts/', include('django.contrib.auth.urls'))
]