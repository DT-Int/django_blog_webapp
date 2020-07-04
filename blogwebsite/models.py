from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


class Post(models.Model):
	title = models.CharField(max_length=100)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()
	post_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title + " | " + str(self.author)

	def get_absolute_url(self): #to define where to go after hitting Post
		return reverse('article_details', args=(str(self.id)))