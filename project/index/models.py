from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User, related_name='userposts', on_delete=models.CASCADE, blank=True)
    image1 = models.FileField(blank=True, null=True)
    image2 = models.FileField(blank=True, null=True)
    image3 = models.FileField(blank=True, null=True)
    image4 = models.FileField(blank=True, null=True)
    image5 = models.FileField(blank=True, null=True)
    image6 = models.FileField(blank=True, null=True)
    image7 = models.FileField(blank=True, null=True)
    image8 = models.FileField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    # user = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
    details = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = '-created'

    # def save(self, *args, **kwargs):
    # 	# self.slug = self.cinema_name
    # 	qs = User.objects.get(username = self.username)
    # 	self.user = qs
    # 	super (Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='postcomment', on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, related_name='usercomment', on_delete=models.CASCADE, blank=True)
    comment = models.TextField()

    def __str__(self):
        return self.user.username

class PostFiles(models.Model):
    file = models.FileField(upload_to='postimages')