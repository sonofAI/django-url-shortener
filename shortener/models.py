from django.db import models
from .helphers import generate_short_code

# Create your models here.

class ShortURL(models.Model):
    full_url = models.URLField()
    short_url = models.CharField(max_length=6, unique=True, default=generate_short_code)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.short_url} -> {self.full_url}'