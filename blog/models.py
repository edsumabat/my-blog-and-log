from django.db import models

class Blog(models.Model):
    """The blog of a user."""
    name = models.TextField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Blog_Post(models.Model):
    """Individual blog post."""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return [self.title, self.body]