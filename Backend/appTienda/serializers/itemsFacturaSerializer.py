from appTienda.models.itemsFactura import ItemsFactura
from rest_framework import serializers

class ItemsFacturaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model: ItemsFactura
        fields = ['unidades', 'subtotal']