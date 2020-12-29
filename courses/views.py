from django.shortcuts import render
from rest_framework import viewsets
from .models import Productos
from .serializers import CourseSerializer

class ProductViews(viewsets.ModelViewSet):
	queryset = Productos.objects.all()
	serializer_class = CourseSerializer