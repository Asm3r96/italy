from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models



# Create your models here.


class Meal(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='images/', blank=True, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
     

    def __str__(self):
        return f"{self.title} {self.description}"

    def __str__(self):
        return str(self.title) + ": €" + str(self.price)


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'catiegory'
        verbose_name_plural = 'catiegories'

    def __str__(self):
        return f"{self.name}"

    




