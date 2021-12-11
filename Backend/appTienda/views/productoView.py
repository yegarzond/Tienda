from django.conf import settings
from rest_framework import generics,  status, views
from appTienda.models.producto import Producto
from appTienda.serializers.productoSerializer import ProductoSerializer
from rest_framework import status, views, generics
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend

from appTienda.models.producto import Producto
from appTienda.serializers.productoSerializer import ProductoSerializer

class ProductoView(generics.ListAPIView):
    queryset           = Producto.objects.all()
    serializer_class   = ProductoSerializer
    def get_queryset(self):
        return super().get_queryset()