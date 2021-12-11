from tienda import settings

from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend

from appTienda.models.producto import Producto
from appTienda.serializers.productoSerializer import ProductoSerializer
from appTienda.serializers.productoUpdateSerializer import ProductoUpdateSerializer

class ProductoDetailView(views.APIView):
    productos = Producto.objects.all()

    def get(self, request, *args, **kwargs):
        producto = self.productos.get(id = kwargs['pk'])

        if (producto):
            producto_serializer = ProductoSerializer(producto)
            return Response(producto_serializer.data, status = status.HTTP_200_OK)

        return Response({ 'message': 'Producto no encontrado' }, status=status.HTTP_404_NOT_FOUND) 

    def put(self, request, *args, **kwargs):
        producto = self.productos.filter(id = kwargs['pk']).first()

        if(producto):
            producto_serializer = ProductoUpdateSerializer(producto, data = request.data)

            if(producto_serializer.is_valid(raise_exception = True)):
                producto_serializer.save
                return Response({'message': 'Producto actualizado'}, status = status.HTTP_200_OK)
            
            return Response({'message': 'Detalles no válidos'}, status = status.HTTP_400_BAD_REQUEST)
        
        return Response({'message': 'Producto no encontrado'}, status = status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, *args, **kwargs):
        producto = self.productos.filter(id = kwargs['pk']).first()

        if(producto):
            producto.delete()
            return Response({'message': 'Producto eliminado'}, status = status.HTTP_200_OK)
        
        return Response({'message': 'Producto no encontrado'}, status = status.HTTP_404_NOT_FOUND)