from django import forms

from .models import Blog, Blog_Post

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name']

class Blog_Post_Form(forms.ModelForm):
    class Meta:
        model = Blog_Post
        fields = ['title', 'body']
        widgets = {'body': forms.Textarea(attrs={'cols': 80})}