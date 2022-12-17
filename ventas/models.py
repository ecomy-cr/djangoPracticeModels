from django.db import models
from django.utils import timezone
from menu.models import Menu


class Ventas(models.Model):
    fecha = models.DateTimeField(default=timezone.now)
    plato = models.OneToOneField(Menu,  on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    
    def __str__(self):
        colName = f"{self.fecha} - {self.plato} :"
        return colName
    
    

