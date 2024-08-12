from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name = 'home'),
    path('games/', views.GameList.as_view(), name = 'game_list'),
    path('create/game', views.create_game, name = 'create_game'),
    path('create/post', views.create_post, name = 'create_post'),
    path('games/<slug:slug>/', views.game, name='game'),
    path('<slug:slug>/', views.post, name='post'),
    path('edit/<slug:slug>/', views.post_edit, name='post_edit'),
    path('delete/<slug:slug>/', views.post_delete, name='post_delete'),
]

