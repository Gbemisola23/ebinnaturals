from django.urls import path
from .import views
from .views import PostList


urlpatterns = [
    path('', PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('addPost', views.add_post, name='add_post'),
    path('editPost/<slug:slug>/', views.edit_post, name='edit_post'),
    path('deletePost/<slug:slug>/', views.delete_post, name='delete_post'),
    path('<slug:slug>/edit-comment/<slug:comment_id>/', views.edit_comment, name='edit_comment'),
    path('<slug:slug>/delete-comment/<slug:comment_id>', views.delete_comment, name="delete_comment"),
]
