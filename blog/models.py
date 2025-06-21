from django.db import models

# Create your models here.

class BlogModel(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_body = models.TextField()
    
    def __str__(self):
        return self.blog_title
    
    
class CommentModel(models.Model):
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()