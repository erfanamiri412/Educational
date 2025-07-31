from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='profile_path',default='m.jpg')
    
    def __str__(self):
        return self.bio
    
    def get_absolute_url(self):
        return reverse("profile", kwargs={"pk": self.pk})
    

class Education(models.Model):
    school = models.CharField(max_length=30)
    degree = models.CharField(max_length=30)
    field = models.CharField(max_length=30)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True) 
    description = models.TextField()
    
    def __str__(self):
        return self.field
    
    
class Experience(models.Model):
    title = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True) 
    description = models.TextField()
    
    def __str__(self):
        return self.field
    
    
@receiver(post_save , sender=User)
def create_profile(sender,instance,created,**kwargs):
        if created:
            UserProfile.objects.create(user = instance)