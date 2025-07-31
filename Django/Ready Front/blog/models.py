from django.db import models
from django.urls import reverse
from accounts.models import UserProfile
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField()
    slug = models.SlugField(max_length=40,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(UserProfile,related_name='post_like',null=True,blank=True)
    dislike = models.ManyToManyField(UserProfile,related_name='post_dislike',null=True,blank=True)
    
    def __str__(self):
        return f'{self.title}-{self.created_at}'
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.slug})
    
    def save(self,*args, **kwargs):
        super().save()
        if not self.slug:
            self.slug = slugify(self.title)
            self.save()
    
class Comment(models.Model):
    author = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    body = models.TextField()
    is_validate = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.body