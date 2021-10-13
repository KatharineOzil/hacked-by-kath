from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
import sys
from mdeditor.fields import MDTextField

# Create your models here.

## 文章分类
class Category(models.Model):
	category = models.CharField(max_length=20)
	#cover = models.ImageField(upload_to='blog/static/category_cover/', blank=False, default='blog/static/category_cover/default.png')
	
	def __str__(self):
		return self.category


## 文章详情

class Article(models.Model):
	#cover = models.ImageField(upload_to='blog/static/cover/', blank=False)
	title = models.CharField(max_length=100)
	create_time = models.DateField(default=timezone.now)
	update_time = models.DateField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	content = MDTextField()
	visible = models.BooleanField(default=True)
	attachment = models.FileField(upload_to='blog/static/content/', blank=True) 
	#TODO：upload to different folders according to the categories
	#TODO：FileField vs. FilePathField

	def __str__(self):
		return self.title


## User
class User(AbstractUser):
	avater = models.ImageField(upload_to='blog/static/others/', blank=False, default='blog/static/category_cover/default.png')
	github_url = models.URLField(blank=True)
	intro = MDTextField(blank=True, default='GuessWhoAmI!')


## 评论(待定)
class Comment(models.Model):
	pass

## TODO List
class Todo(models.Model):
	title = models.TextField()
	create_time = models.DateField(default=timezone.now)
	is_done = models.BooleanField(default=False)
	finish_time = models.DateField()


