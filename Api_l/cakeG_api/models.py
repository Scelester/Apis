from urllib import request
from django.db import models
from django.urls import reverse


# Create your models here.
class Occation(models.Model):

    name = models.CharField( max_length=50)

    class Meta:
        verbose_name = "occation"
        verbose_name_plural = "occations"

    def __str__(self):
        return self.name


class All_cakes(models.Model):
    name = models.CharField( max_length=500)
    occation = models.ForeignKey(Occation, on_delete=models.CASCADE)
    image = models.ImageField( upload_to='./media',blank=True,null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    