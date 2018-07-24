from django.db import models
from django.conf import settings
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):

	"""Model for blog post, including title, subtitle, author, body, etc."""

	title = models.CharField(max_length=255, db_index=True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
	body = RichTextUploadingField()
	created_at = models.DateTimeField(auto_now_add=True)
	category = models.ForeignKey('blog.Category', on_delete=models.PROTECT)
	image = models.ImageField(blank=True, null=True)

	def __str__(self):
		return self.title

class Category(models.Model):

	"""Model for categories of blog posts, is foreignkey in Post model."""

	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = "Categories"

class Contact(models.Model):

	"""Model for contact me page."""
	
	name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	message = models.CharField(max_length=1000)




