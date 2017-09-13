from django.db import models
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.

class Person(models.Model):
	name = models.CharField(max_length = 400)
	email = models.CharField(max_length = 400)
	title = models.CharField(max_length = 400)
	image = models.CharField(max_length = 400)
	slug = models.SlugField(max_length = 40, blank = True, default = '')
	responsibilties = models.CharField(max_length = 1000)
	bio = models.CharField(max_length = 40)
	github = models.CharField(max_length = 40)
	birthday = models.DateTimeField(default = timezone.now)

	def save(self, *args, **kwargs):
		
		if not self.pk:
			self.slug = slugify(self.name)
		super(Person, self, *args, **kwargs).save()


	def __str__(self):
		return self.name
