from django.db import models

# Create your models here.

class product(models.Model):
    pk_producto = models.AutoField(primary_key=True, null=False, blank=False)
    codigo = models.CharField(max_length=9, null=False, blank=False)
    nombre = models.CharField(max_length=40, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    imagen1 = models.URLField(max_length=800, default='https://i.pinimg.com/736x/3a/ab/e0/3aabe0e9a520b9ad90407a82f85adb42.jpg', null=False, blank=False)
    precio = models.DecimalField(null=False, blank=False, max_digits=7, decimal_places=2)

    class Meta:
        verbose_name='product'
        verbose_name_plural='products'
        ordering=['nombre']

    def __str__(self):
        return "{0}".format(self.nombre)