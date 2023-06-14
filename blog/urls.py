from django.urls import path
from .import views
from .views import PostList


urlpatterns = [
    path('', PostList.as_view(), name='blog'),
#     path('<str:slug>/', views.post_detail, name='post_detail'),
#     path('editPost/<slug:slug>/', views.editPost, name='edit_post'),
#     path('addPost', views.addPost, name='add_post'),
]