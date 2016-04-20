import datetime
from django.db import models

class Blog(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.name

class Author(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField()
	birthday = models.DateField()

	def __str__(self):
		return "{} ({})".format(self.name, self.email)

class Entry(models.Model):
	blog = models.ForeignKey(Blog)
	headline = models.CharField(max_length=255)
	excerpt = models.TextField(blank=True, null=True)
	body = models.TextField()
	authors = models.ManyToManyField(Author)
	pub_date = models.DateTimeField(default=datetime.datetime.now)
	rating = models.FloatField()

	def __str__(self):
		return self.headline
	
class BlogComment(models.Model):
	blog = models.ForeignKey(Blog)
	name = models.CharField(max_length=100)
	comment = models.TextField()
	timestamp = models.DateTimeField(default=datetime.datetime.now)

	def __str__(self):
		return "Comment for {} by {}".format(self.blog, self.name)

