from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(null=False, upload_to="userimages/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=100)
    visible = models.BooleanField(default=False)
    username_visible = models.BooleanField(default=False)
    private = models.BooleanField(default=False)

    def username(self):
        return self.user.username
    
    def __str__(self):
        return self.caption + ", " + self.username()
    
    @property
    def total_likes(self):
        return Likes.objects.filter(image_id=self.id).count()
    
    @property
    def total_comments(self):
        return Comments.objects.filter(image_id=self.id).count()


class Likes(models.Model):
    id = models.AutoField(primary_key=True)
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.TextField()
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Deleted_Comments(models.Model):
    id = models.AutoField(primary_key=True)
    commented_user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return f"user: {self.commented_user}, comment: {self.content}"
