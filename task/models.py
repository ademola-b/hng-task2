from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
import re

# Create your models here.

def validate_no_numbers(value):
    if any(char.isdigit() for char in value):
        print("not allowed")
        raise ValidationError("Numbers are not allowed in this field.")

class Person(models.Model):
    name = models.CharField(unique=True, max_length=50, validators=[validate_no_numbers])
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=1000)
