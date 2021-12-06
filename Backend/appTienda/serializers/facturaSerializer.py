from rest_framework import serializers

from appTienda.serializers.userSerializer import UserSerializer
from appTienda.serializers.itemsFactura import ItemsFactura
from appTienda.serializer.producto import ProductoSerializer

from appTienda.models.factura import Factura
from appTienda.models.itemsFactura import itemsFactura
from appTienda.models.producto import producto
from appTienda.models.user import User


class FacturaSerializer(serializer.ModelSerializer):


    itemsFactura = ItemsFacturaSerializer()


    class Meta:
        model: factura
        fields: ['id','fecha','tipo_doc','num_doc', 'nombres','apellidos','total_items','total_factura','itemsFactura']

    def create(self, validated_data):
        itemsFactura_data = validated_data.pop('itemsFactura')
        facturaInstance = Factura.objects.create(**validated_data)
        itemsFactura.objects.create(factura = facturaInstance, **itemsFactura_data)
        return facturaInstance
         
    def to_representation(self, obj):
        factura = Factura.objects.get(id = obj.id)
        itemsFactura = ItemsFactura.objects.get(itemsFactura = obj.id)
        return {
            
            'fecha': factura.fecha, 
            'total_items': factura.total_items,
            'total_factura': factura.total_factura,
            'itemsFactura':{
                'unidades': itemsFactura.unidades,
                'precio': itemsFactura.precio,
                'subtotal': itemsFactura.subtotal
            }
        }

