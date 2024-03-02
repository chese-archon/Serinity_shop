from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Product(models.Model):
    """Товар"""

    name = models.CharField(verbose_name='Название', max_length=128)
    price = models.IntegerField(default=0) #цена
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    depth = models.IntegerField(default=0)
    description = models.TextField(default='') #описание
    image = models.ImageField(upload_to='product_images', null=True) #Фотография товара

    #def new_image(self, data):
    #    product_image = ProductImage()
    #    product_image.product = self
    #    product_image.image = data['image']
    #    product_image.save()

    def __str__(self):
        return self.name

# у каждого товара может быть неограниченное количество фотографий
#class ProductImage(models.Model):
#    """Фотография товара"""
#
#    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
#    image = models.ImageField(upload_to='app_redesign/static/product_images', null=True)