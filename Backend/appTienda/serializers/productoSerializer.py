from appTienda.models.producto import Producto
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model: Producto
        fields = ['ref', 'nombre', 'marca', 'unidad_medida', 'precio']