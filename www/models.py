from django.db import models

# Create your models here.

class Person(models.Model):
	name = models.CharField(max_length = 400)
	email = models.CharField(max_length = 400)
	title = models.CharField(max_length = 400)
	image = models.CharField(max_length = 400)

	def __str__(self):
		return self.name
