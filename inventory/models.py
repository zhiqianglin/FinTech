from django.db import models

# Create your models here.

from django.db import models
from django.forms import URLField


class Restaurant(models.Model):
	name = models.CharField(max_length = 200)
	offer = models.TextField(default="N/A")
	# offer = models.DecimalField(max_digits = 6, decimal_places = 2, default=0)
	# description = models.TextField()
	# priceLevel = models.IntegerField()
	# category = models.TextField()
	# address = models.TextField()

	image = models.TextField(max_length = 200, default='N/A')
	# image = URLField(max_length = 200)
	rating = models.DecimalField(max_digits=2, decimal_places=1)
	url = models.TextField()

	@classmethod
	# def create(cls, name, description, priceLevel, category, address, rating):
	# 	res = cls(name = name, description = description,
	# 	priceLevel = priceLevel, category = category,
	# 	address = address,rating = rating)
	# 	print("Book %s created" % priceLevel)
	# 	return res

	def create(cls, name, offer, rating, image, url):
		res = cls(name = name, offer = offer,
			rating = rating, image = image, url=url)

		print("Book %s created" % name)
		return res

