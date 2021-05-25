from django.db import models

# Create your models here.


class backgroundImage(models.Model):
    imageName = models.CharField(max_length=254, null=True, blank=True)
    Image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.imageName


class breadcrumbs(models.Model):
    breadcrumbName = models.CharField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.breadcrumbName


class frames(models.Model):
    frameHeader = models.CharField(max_length=254, null=True, blank=True)
    frameInfo = models.CharField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.frameHeader


class headline(models.Model):
    headlineHeader = models.CharField(max_length=254, null=True, blank=True)
    headlineQuote = models.CharField(max_length=254, null=True, blank=True)
    headlineName = models.CharField(max_length=254, null=True, blank=True)
    headlineEducation = models.CharField(max_length=254, null=True, blank=True)
    
    def __str__(self):
        return self.headlineHeader

