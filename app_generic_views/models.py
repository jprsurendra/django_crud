from django.db import models
from django.urls import reverse

class BookCategory(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name