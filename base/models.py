from django.db import models
from autoslug import AutoSlugField
from pytils.translit import slugify
from django.conf import settings
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User

class BlogEntry(models.Model):
    caption = models.CharField(max_length=255)
    text = models.TextField()
    pinned = models.BooleanField()
    creation_ts = models.DateField(auto_now_add = True)
    def __str__(self):
        return self.caption

class Gallery(models.Model):
    photo = ImageField(null=True, blank=True)
    comment = models.CharField(max_length=255)
    creation_ts = models.DateField(auto_now_add = True)

class RoadMap(models.Model):
    text        = models.TextField()
    status      = models.BooleanField()
    creation_ts = models.DateField(auto_now_add = True)
    comment     = models.TextField()

class Bug(models.Model):
    text        = models.TextField()
    status      = models.BooleanField()
    creation_ts = models.DateField(auto_now_add = True)
    comment     = models.CharField(max_length=255)

class StaffItem(models.Model):
    caption        = models.CharField(max_length=255)
    text           = models.TextField()

class ProgressItem(models.Model):
    caption        = models.CharField(max_length=255)
    value          = models.IntegerField(default=0)

class SceneFeature(models.Model):
    caption        = models.CharField(max_length=255)
    text           = models.TextField()
    def __str__(self):
        return self.caption
# Create your models here.
