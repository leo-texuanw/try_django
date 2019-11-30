from django.db import models


class Goal(models.Model):
    name = models.CharField(max_length=120)
    content = models.TextField()

    def __str__(self):
        return self.name