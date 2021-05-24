from django.db import models

# Create your models here.


class backgroundImage(models.Model):
    Image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.Image