from django.db import models


class datas(models.Model):
	city= models.CharField(max_length=200,unique=True)
	weather = models.CharField(max_length=10)
	tempreture = models.FloatField(max_length=10)
	Humidity = models.FloatField(max_length=20)
	lon=models.FloatField(max_length=10,null=True)
	lat=models.FloatField(max_length=10,null=True)


	def __str__(self):
		return self.city
