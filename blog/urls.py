from django.urls import path
from .import views
from .views import PostList


urlpatterns = [
    path('', PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('addPost', views.addPost, name='add_post'),
    path('editPost/<slug:slug>/', views.editPost, name='edit_post'),
    path('deletePost/<slug:slug>/', views.deletePost, name='delete_post'),

    path('<slug:slug>/add_comment', views.add_comment, name='add_comment'),
    path('<slug:slug>/edit-comment/<slug:commentId>/', views.edit_comment, name='edit_comment'),
    path('<slug:slug>/delete-comment/<slug:commentId>', views.delete_comment, name="delete_comment"),
]
