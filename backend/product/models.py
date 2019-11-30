"""
Execute this every time modify this file:
    $ python manage.py makemigrations
    $ python manage.py migrate
"""
from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=120)    # max_length is required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField()    # null=True, default=True

    def get_absolute_url(self):
        # return f"/product/{self.id}"

        # product-lookup is defined as a name in urls.py
        return reverse("product:product-lookup", kwargs={"my_id": self.id})
