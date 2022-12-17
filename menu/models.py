from django.db import models


# Create your models here.
class Menu(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.FloatField()
    imagen = models.ImageField(default='batman.png')
    detalle = models.TextField()
    
    def __str__(self):
        colName = f"{self.nombre}: c.{self.precio}"
        return colName
    
    

