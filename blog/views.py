from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView
from django.views.decorators.http import require_POST
from . import views
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostForm, AddPostForm, CommentForm
from .models import Post, Comment


class PostList(ListView):
    """view to create the post on the blog"""
    model = Post
    template_name = 'blog/blog.html'

def post_detail(request, slug, commented=False, commentForm=CommentForm()):
    """ View to show a particular blog post in detail """
    queryset = Post.objects
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.filter(approved=True).order_by("-created_on")

    template = 'blog/post_detail.html'
    context = {
        'post': post,
        'comments': comments,
        'commented': commented,
        'comment_form': commentForm
    }

    return render(request, template, context)
    
@login_required
@require_POST
def add_comment(request, slug):
    """ View to show a particular blog post in detail """
    queryset = Post.objects
    post = get_object_or_404(queryset, slug=slug)

    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment_form.instance.user = request.user
        comment_form.instance.name = request.user.username
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.save()
        commented = True

    return post_detail(request, slug, True)

@login_required
def edit_comment(request, slug, commentId):
    """ View to show a particular blog post in detail """
    queryset = Post.objects
    post = get_object_or_404(queryset, slug=slug)
    comment = post.comments.filter(approved=True, id=commentId).first()

    if comment:
        commentForm = CommentForm(instance=comment)
    else:
        commentForm = None

    return post_detail(request, slug, commentForm=commentForm)

@login_required
def delete_comment(request, slug, commentId):
    """
    A view to delete comments by admin
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'You are not authorized to perform this action!!')
        return redirect(
            reverse('blog'))

    comment = get_object_or_404(Comment, pk=commentId)
    comment.delete()
    messages.success(request, 'The comment was removed!')
    
    return redirect(reverse('post_detail', args=[slug]))


@login_required
def editPost(request, slug):
    """
    A view for admin to edit blog posts

    """
    if not request.user.is_superuser:
        messages.error(
            request, 'You are not authorized to perform this action!')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        postForm = PostForm(request.POST, request.FILES, instance=post)
        if postForm.is_valid():
            postForm.save()
            messages.success(request, 'Successfully updated the post!')
            return redirect('blog')
        else:
            messages.error(request, 'Failed to update the post. \
                Please ensure the form is valid.')

    else:
        postForm = PostForm(instance=post)
        messages.info(
            request, f'You are currently in editing mode: {post.slug}')

    template = 'blog/edit_post.html'
    context = {
        'postForm': postForm,
        'post': post,
    }

    return render(request, template, context)


@login_required
def deletePost(request, slug):
    """
    A view to delete posts
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'You are not authorized to perform this action!!')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, 'The post was deleted!')
    return redirect(reverse('blog'))


@login_required
def addPost(request, ):

    """
    A view to add blog post &

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
