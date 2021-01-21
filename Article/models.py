from django.db import models
from tinymce.models import HTMLField
from Users.models import UserProfile
from django.db.models import signals


class Post(models.Model):

    description = models.CharField(max_length=50)
    content = HTMLField()
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class LikeReaction(models.Model):

    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)

class Comments(models.Model):

    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    comment = models.TextField()

def update_likes(sender,instance,created,**kwargs):
    if created:
        instance.post.likes += 1
        instance.post.save()

signals.post_save.connect(receiver=update_likes, sender=LikeReaction)



