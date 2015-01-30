from django.db import models
from django.template.defaultfilters import slugify
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.

class PostManager(models.Manager):
    def all(self):
        return super(PostManager, self).filter(publish=True)

# Category Model
class Category(models.Model):
	title = models.CharField(max_length=65)
	slug = models.SlugField(unique=True)
	description = models.TextField(max_length=155)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('category', args=[str(self.slug)])

# Post Model
class Post(models.Model):
	publish = models.BooleanField(default=False)
	author = models.ForeignKey(User)
	categories = models.ManyToManyField(Category)
	author = models.ForeignKey(User)
	title = models.CharField(max_length=65)
	slug = models.SlugField(unique=True)
	description = models.TextField(max_length=140)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return smart_unicode(self.title)

	def get_previous_by_post(self):
		return self.get_previous_by_timestamp()

	def get_next_post(self):
		return self.get_next_by_timestamp()

	class Meta:
		verbose_name = 'Blog Entry'
		verbose_name_plural = 'Blog Entries'
		ordering = []`