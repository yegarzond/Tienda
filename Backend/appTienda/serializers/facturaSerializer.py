from appTienda.models.factura import Factura
from rest_framework import serializers

class FacturaSerializer(serializer.ModelSerializer):
    class Meta:
        model: factura
        fields: ['id','fecha','tipo_doc','num_doc','nombres', 'apellidos', 'total_items','total_factura']