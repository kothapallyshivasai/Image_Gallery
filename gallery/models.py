from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(null=False, upload_to="userimages/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=100)
    visible = models.BooleanField(default=True)
    username_visible = models.BooleanField(default=True)

    def username(self):
        return self.user.username
    
    def __str__(self):
        return self.caption + ", " + self.username()
    
    @property
    def total_likes(self):
        return Likes.objects.filter(image_id=self.id).count()


class Likes(models.Model):
    id = models.AutoField(primary_key=True)
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
