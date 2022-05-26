from django.db import models

# Create your models here.


class FeedBack(models.Model):
    name = models.CharField('', max_length=80)
    email = models.CharField('', max_length=100)
    message = models.TextField('')

    def __str__(self):
        return self.name


class Photo(models.Model):
    image = models.ImageField(null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


