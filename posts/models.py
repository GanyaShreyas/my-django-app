from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/%y/%m/%d',default='media/users/2024/0706/default-profile-photo.jpg')
    caption = models.TextField(blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,blank=True)
    created =models.DateField(auto_now=True)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='posts_liked',blank=True) 
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super().save(*args,**kwargs)


""" 
we need to add the posts in order of the time and date they posted. 
we implement the comment order using a meta class. similarly need to implement the posts feed based on date and time

"""

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.body