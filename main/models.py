from django.db import models

# Create your models here.
class Contact(models.Model):

    name = models.CharField("Name", max_length=50)
    lastname = models.CharField("Lastname", max_length=50)
    email = models.EmailField("Email", max_length=254)
    topic = models.CharField("Topic", max_length=200)
    content = models.TextField("Text")


    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return f"{self.name} | {self.topic}"