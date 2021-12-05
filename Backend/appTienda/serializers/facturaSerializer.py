from rest_framework import serializers

from appTienda.serializers.userSerializer import UserSerializer
from appTienda.serializers.itemsFactura import ItemsFactura
from appTienda.serializer.producto import ProductoSerializer

from appTienda.models.factura import Factura
from appTienda.models.itemsFactura import itemsFactura
from appTienda.models.producto import producto
from appTienda.models.user import User


class FacturaSerializer(serializer.ModelSerializer):

    user = UserSerializer()
    itemsFactura = ItemsFacturaSerializer()
    producto = ProductoSerializer()

    class Meta:
        model: factura
        fields: ['id','fecha','tipo_doc','num_doc', 'nombres','apellidos','total_items','total_factura', 'user','itemsFactura', 'producto']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        facturaInstance = Factura.objects.create(**validated_data)
        User.objects.create(factura = facturaInstance, **user_data)
        return facturaInstance
    
    def create(self, validated_data):
        itemsFactura_data = validated_data.pop('itemsFactura')
        facturaInstance = Factura.objects.create(**validated_data)
        ItemsFactura.objects.create(factura = facturaInstance, **itemsFactura_data)
        return facturaInstance
    
    def to_representation(self, obj):
        factura = Factura.objects.get(id = obj.id)
        user = User.objects.get(factura = obj.id)
        itemsFactura = ItemsFactura.objects.get(factura = obj.id)
        return {
            
            'fecha': factura.fecha,

            'user': {
                'name': user.name,
                'email': user.mail,
            },

            'producto': {
                'ref': producto.ref,
                'nombre': producto.nombre,
                'marca': producto.marca,
                'unidad_medida': producto.unidad_medida,
                'precio': producto.precio
            },

            'itemsFactura':{
                'unidades': itemsFactura.unidades,
                'precio': itemsFactura.precio,
                'subtotal': itemsFactura.subtotal
            },

            'total_items': factura.total_items,
            'total_factura': factura.total_factura
        }

