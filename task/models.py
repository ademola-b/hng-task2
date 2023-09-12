from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Person(models.Model):
    name = models.CharField(unique=True, max_length=50)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=1000)
