from django.db import models

# Create your models here.


class backgroundImage(models.Model):
    imageName = models.CharField(max_length=254, null=True, blank=True)
    Image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.imageName
