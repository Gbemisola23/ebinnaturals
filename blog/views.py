# from django.shortcuts import render, redirect, reverse, get_object_or_404
# from django.urls import reverse_lazy
from django.views.generic import ListView
from . import views
from django.contrib import messages
from .forms import PostForm
from .models import Post, Comment


class PostList(ListView):
    model = Post
    template_name = "blog/blog.html"

def post_detail(request, slug):
    """ View to show a particular blog post in detail """

    post = BlogPost.objects.filter(slug=slug).first()
    comments = Comment.objects.filter(blog_id=post)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'Action not allowed')
            return redirect(reverse('home'))
        else:
            user = request.user
            body = request.POST.get('body', '')
            comment = Comment(user=user, body=body, blog_id=post)
            comment.save()

    template = 'blog/post_detail.html'
    context = {
        'post': post,
        'comments': comments,
    }

    return render(request, template, context)

def addPost(request, ):

    """
    A view to add blog post

    """
    if not request.user.is_superuser:
        messages.error(
             request, 'You are not authorized to perform this action!!')
        return redirect(reverse('home'))

    template = 'blog/add_post.html'

    form = AddPostForm(request.POST or None, request.FILES or None)

    context = {
         'form': form,
     }

    if request.method == "POST":
        form = AddPostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            messages.success(
                request, 'A new blog has been successfully added')
            return redirect('blog')
        else:
            messages.error(
                request, 'An error occurred. \
                    Please ensure the form is valid.')
    else:
        form = AddPostForm()

    return render(request, template, context)
