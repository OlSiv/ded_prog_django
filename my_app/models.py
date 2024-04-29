from django.db import models


class Worker(models.Model):
	name = models.CharField(max_length=20, blank=False)
	second_name = models.CharField(max_length=35, blank=False)
	salary = models.IntegerField(default=0)
