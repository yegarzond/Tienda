from appTienda.models.user import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    factura = FacturaSerializer()
    class Meta:
        model: User
        fields = ['']

