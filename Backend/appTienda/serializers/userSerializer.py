from appTienda.models.user import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    factura = FacturaSerializer()
    class Meta:
        model: User
        fields = ['id', 'username', 'password', 'name', 'email']

    def create(self, validated_data):
        factura_data = validated_data.pop('factura')
        userInstance = User.objects.create(**validated_data)
        Factura.objects.create(user = userInstance, **factura_data)
        return factura_data

        
    
    def to_representation(self, obj):
        user = User.objects.get(id = obj.id)
        factura = Factura.objects.get(user = obj.id)
        return {
            'id' = user.id,
            'username' = user.username,
            'name' = user.name,
            'email' = user.email,
            ''
        }
