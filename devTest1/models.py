from django.db import models

# Create your models here.


class Feature(models.Model):
    featureCategory = models.CharField(max_length=254, null=True, blank=True)
    feautureTitle = models.CharField(max_length=254, null=True, blank=True)
    featureDesc = models.CharField(max_length=254, null=True, blank=True)
    featureImage = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.featureCategory


class Insights(models.Model):
    insightsCategory = models.CharField(max_length=254, null=True, blank=True)
    insightsTitle = models.CharField(max_length=254, null=True, blank=True)
    insightsDesc = models.TextField(max_length=254, null=True, blank=True)
    insightsImage = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.insightsCategory