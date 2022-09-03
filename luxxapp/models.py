from django.conf import settings
from django.db import models
from django.utils import timezone


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    category = models.CharField(max_length=200)
   
    def __str__(self):
        return self.name

