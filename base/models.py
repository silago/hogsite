from django.db import models
from autoslug import AutoSlugField
from pytils.translit import slugify
from django.conf import settings
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User

class BlogEntry(models.Model):
    caption = models.TextField()
    text = models.TextField()
    pinned = models.BooleanField()
    creation_ts = models.DateField(auto_now_add = True)

class Gallery(models.Model):
    photo = ImageField(null=True, blank=True)
    comment = models.TextField()
    creation_ts = models.DateField(auto_now_add = True)

class RoadMap(models.Model):
    text        = models.TextField()
    status      = models.TextField()
    creation_ts = models.DateField(auto_now_add = True)
    comment     = models.TextField()

class Bug(models.Model):
    text        = models.TextField()
    status      = models.TextField()
    creation_ts = models.DateField(auto_now_add = True)
    comment     = models.TextField()

class StaffItem(models.Model):
    caption        = models.TextField()
    text           = models.TextField()

# Create your models here.
