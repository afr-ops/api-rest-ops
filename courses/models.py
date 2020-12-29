from django.db import models

class Productos(models.Model):
	codigo = models.CharField(max_length=200)
	producto = models.CharField(max_length=100)
	precio = models.CharField(max_length=100)
	descuento = models.CharField(max_length=10)

	def __str__(self):
		return self.nombre 
