"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quotes.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]"""
from django.contrib import admin
from django.urls import path, include
from quotes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('tag/<str:tag_name>/', views.tag_search, name='tag'),
    path('register/', views.register, name='register'),
    path('add/', views.add_quote, name='add_quote'),

    path('accounts/', include('django.contrib.auth.urls')),
]