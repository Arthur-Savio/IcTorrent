from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField, JSONField

class File(models.Model):
    name = models.CharField(max_length=100)
    length = models.IntegerField()
    info = ArrayField(JSONField())
    date = models.DateField()
    seeders = models.IntegerField()