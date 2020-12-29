from rest_framework import serializers
from .models import Productos

class CourseSerializer(serializers.HyperlinkedModelSerializer): 	

	class Meta:
		model = Productos
		fields = ('id', 'codigo', 'producto', 'precio', 'descuento')

