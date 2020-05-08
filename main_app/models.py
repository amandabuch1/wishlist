from django.db import models

# Create your models here.
class Wish(models.Model):
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.description