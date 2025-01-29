from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    # Home page with different user blogs.
    path('', views.index, name='index'),
    # Show all blogs.
    path('blogs/', views.blogs, name='blogs'),
    # Show individual blog posts of a blog.
    path('blogs/<int:blog_id>', views.blog, name='blog'),
    # Page for adding a new blog.
    path('new_blog/', views.new_blog, name='new_blog'),
]