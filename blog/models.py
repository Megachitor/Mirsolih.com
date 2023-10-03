from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):

    name = models.CharField("Name", max_length=50)

    class Meta:
        verbose_name = ("Tag")
        verbose_name_plural = ("Tags")

    def __str__(self):
        return self.name

class Post(models.Model):

    Status = ("Not saved", "In progress", "Published")

    name = models.CharField("Name", max_length=50)
    content = models.TextField("Content")
    image = models.ImageField("Image", upload_to=None, height_field=None, width_field=None, max_length=None)
    date = models.DateTimeField("Date", auto_now=False, auto_now_add=True)
    status = models.CharField("Status", max_length=15,choices=Status, default=1)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    likes = models.IntegerField("Likes")
    views = models.IntegerField("Views")
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.name

class Comment(models.Model):

    name = models.CharField("Name", max_length=50)
    content = models.TextField("Content")
    email = models.EmailField("Email", max_length=254)
    date = models.DateField("Date", auto_now=False, auto_now_add=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Comment")
        verbose_name_plural = ("Comments")

    def __str__(self):
        return f"{self.name} | {self.post}"


