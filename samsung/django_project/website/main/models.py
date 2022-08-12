from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name of product")
    description = models.TextField()
    cost = models.FloatField()
    available_amount = models.IntegerField()
    volume_type = models.ForeignKey('VolumeType', on_delete=models.SET_NULL,null=True)


    def __str__(self):
        return f"{self.name} - {self.description}"


class VolumeType(models.Model):
    name = models.CharField(max_length=30)


class Comment(models.Model):
    username = models.CharField(max_length=100)
    text = models.TextField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.username} : {self.text}"