from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django_ckeditor_5.fields import CKEditor5Field

class Article(models.Model):
    title = models.CharField(max_length=150)
    body = CKEditor5Field()
    photo = models.ImageField(upload_to='post_pics/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    likes = models.ManyToManyField(get_user_model(), related_name='liked_posts', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args = [str(self.id)])

    def total_likes(self):
        return self.likes.count()
    
    def total_comments(self):
        return self.comments.count()

class Comment(models.Model):
    post = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.post.title}"