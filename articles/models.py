from django.conf import settings 
from django.db import models 
from django.urls import reverse 

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title 
    
    # AUTH_USER_MODEL makes sense for references within a models.py file.
    # get_user_model() is reccomended for everwhere else, such as views, tests, etc. 
    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})

class Comment(models.Model):
    # article has a many to one relationship with comments. 
    # the side with the many has a foriegnkey charfield.
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length = 140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse("article_list")
    