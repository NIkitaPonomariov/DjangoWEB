from django.contrib import admin
from django.urls import path, include
from quotes import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.main, name='main'),

    path('tag/<str:tag_name>/', views.tag_search, name='tag'),

    path('register/', views.register, name='register'),

    path('add/', views.add_quote, name='add_quote'),

    path('add-author/', views.add_author, name='add_author'),

    path('add-tag/', views.add_tag, name='add_tag'),

    path('author/<int:id>/', views.author_detail, name='author_detail'),

    path('accounts/', include('django.contrib.auth.urls')),
]