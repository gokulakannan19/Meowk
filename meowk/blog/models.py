from django.db import models
from django.contrib.auth.models import User


class Blogger(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    CATEGORY = (
        ('Tech', 'Tech'),
        ('Social', 'Social')
    )

    blogger = models.ForeignKey(Blogger, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, null=True)
    body = models.TextField(max_length=100000000000000, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
