from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField("Name", max_length=50)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categorys")

    def __str__(self):
        return self.name




class Portfolio(models.Model):

    Status = ("Not saved", "In progress", "Published")

    name = models.CharField("Name", max_length=50)
    content = models.TextField("Content")
    image = models.ImageField("Image", upload_to=None, height_field=None, width_field=None, max_length=None)
    date = models.DateTimeField("Date", auto_now=False, auto_now_add=True)
    status = models.CharField("Status", max_length=15,choices=Status, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Portfolio")
        verbose_name_plural = ("Portfolios")

    def __str__(self):
        return self.name



