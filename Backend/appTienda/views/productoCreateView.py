from rest_framework import status, views
from rest_framework.response import Response
from appTienda.serializers.productoSerializer import ProductoSerializer

class ProductoCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = ProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Producto creado', status = status.HTTP_200_OK)