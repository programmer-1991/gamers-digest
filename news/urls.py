from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name = 'home'),
    path('games/', views.GameList.as_view(), name = 'game_list'),
    path('create/post', views.create_post, name = 'create_post'),
    path('create/game', views.create_game, name = 'create_game'),
    path('<slug:slug>/', views.post, name='post'),
    path('games/<slug:slug>/', views.game, name='game'),
    path('edit/<slug:slug>/', views.post_edit, name='post_edit'),
    path('edit/game/<slug:slug>/', views.game_edit, name='game_edit'),
    path('delete/<slug:slug>/', views.post_delete, name='post_delete'),
    path('delete/game/<slug:slug>/', views.game_delete, name='game_delete'),

]
