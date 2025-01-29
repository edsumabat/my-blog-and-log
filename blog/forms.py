from django import forms

from .models import Blog, Blog_Post

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['text']
        labels = {'text':''}

class Blog_Post_Form(forms.ModelForm):
    class Meta:
        model = Blog_Post
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}