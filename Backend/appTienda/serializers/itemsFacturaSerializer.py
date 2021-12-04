from appTienda.models.itemsFactura import ItemsFactura
from rest_framework import serializers

class ItemsFacturaSerializer(serializers.ModelSerializer):
    factura = FacturaSerializer()
    class Meta:
        model: ItemsFactura
        fields = ['id', 'username', 'password', 'name', 'email']