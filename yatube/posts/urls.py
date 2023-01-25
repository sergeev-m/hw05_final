from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('group/<slug:slug>/', views.GroupPosts.as_view(), name='group_list'),
    path('profile/<str:username>/', views.Profile.as_view(), name='profile'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('follow/', views.FollowIndex.as_view(), name='follow_index'),
    path(
        'posts/<int:pk>/comment/',
        views.add_comment,
        name='add_comment'
    ),
    path(
        'profile/<str:username>/follow/',
        views.profile_follow,
        name='profile_follow'
    ),
    path(
        'profile/<str:username>/unfollow/',
        views.profile_unfollow,
        name='profile_unfollow'
    ),
]
