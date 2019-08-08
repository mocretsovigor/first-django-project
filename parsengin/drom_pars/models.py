from django.db import models

# Create your models here.
class ParsingDB(models.Model):
    href = models.SlugField(max_length=255)

    def __str__(self):
        return str(self.id)
