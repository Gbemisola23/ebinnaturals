from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
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
