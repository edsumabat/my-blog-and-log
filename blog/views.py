from django.shortcuts import render, redirect

from .models import Blog
from .forms import BlogForm, Blog_Post_Form

def index(request):
    """The home page for My Blog."""
    return render(request, 'blog/index.html')


def blogs(request):
    """Display all blogs."""
    blogs = Blog.objects.all()
    context = {'blogs': blogs,}
    return render(request, 'blog/blogs.html', context)


def blog(request, blog_id):
    """Display all individual blog posts."""
    blog = Blog.objects.get(id=blog_id)
    posts = blog.blog_post_set.all()
    context = {'blog': blog, 'posts': posts}
    return render(request, 'blog/blog.html', context)


def new_blog(request):
    """Add a new blog."""
    if request.method != 'POST':
        # No data submitted; create a blank from.
        form = BlogForm()
    else:
        # POST data submitted; process data.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:blogs')
    
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blog/new_blog.html', context)


def new_blog_post(request, blog_id):
    """Add a new blog post."""
    blog = Blog.objects.get(id=blog_id)

    if request.method != 'POST':
        # No data submitted; create a blank from.
        form = Blog_Post_Form()
    else:
        # POST data submitted; process data.
        form = Blog_Post_Form(data=request.POST)
        if form.is_valid():
            new_blog_post = form.save(commit=False)
            new_blog_post.blog = blog
            return redirect('blog:blog')
    
    # Display a blank or invalid form.
    context = {'blog': blog, 'form': form}
    return render(request, 'blog/new_blog_post.html', context)