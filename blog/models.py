from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import *
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
import sys

# Create your models here.

## 文章分类
class Category(models.Model):
	category = models.CharField(max_length=20)
	#cover = models.ImageField(upload_to='blog/static/category_cover/', blank=False, default='blog/static/category_cover/default.png')
	
	def __str__(self):
		return self.category


## 文章详情
class Articles(models.Model):
	#cover = models.ImageField(upload_to='blog/static/cover/', blank=False)
	title = models.CharField(max_length=100)
	create_time = models.DateField(default=timezone.now)
	update_time = models.DateField(default=timezone.now)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	content = models.TextField()
	visible = models.BooleanField(default=True)
	
	def __str__(self):
		return self.title


## User
class User(AbstractBaseUser):
	intro = models.TextField(blank=True, default='GuessWhoAmI!')


## 评论(待定)
class Comment(models.Model):
	pass