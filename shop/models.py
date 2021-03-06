from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    artic = models.TextField()
    color = models.TextField()
    size = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.author


from django.db import models


class Person(models.Model):
    articul = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    adress = models.CharField(max_length=20)