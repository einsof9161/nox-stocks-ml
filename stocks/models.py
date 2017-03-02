from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Stock(models.Model):
    number = models.CharField(max_length=200)
    name   = models.CharField(max_length=1000)
    create_date = models.DateTimeField('date published')

    def save(self, *args, **kwargs):
        if not self.id:
        	self.create_date = timezone.now()
        return super(Stock, self).save(*args, **kwargs)

    def __str__(self):
    	return self.number+"_"+self.name