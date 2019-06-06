"""
Execute this every time modify this file:
    $ python manage.py makemigrations
    $ python manage.py migrate
"""
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120)    # max_length is required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField()    # null=True, default=True
