from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name = 'home'),
    path('create/', views.create, name = 'create'),
    path('game/<slug:slug>/', views.game, name='game'),
    path('<slug:slug>/', views.post, name='post'),
    
]