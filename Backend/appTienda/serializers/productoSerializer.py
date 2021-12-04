from appTienda.models.producto import Producto
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    factura = FacturaSerializer()
    class Meta:
        model: Producto
        fields = ['id', 'username', 'password', 'name', 'email']