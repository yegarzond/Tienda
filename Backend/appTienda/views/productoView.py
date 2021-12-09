from django.conf import settings
from rest_framework import generics,  status, views
from rest_framework.response import Response
from appTienda.models.producto import Producto
from appTienda.serializers.productoSerializer import ProductoSerializer
class CreateProductoView(views.APIView):
    queryset=Producto.objects.all()
    serializer_class= ProductoSerializer
    def post(self, request, *args, **kwargs):
        serializer=ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        stringResponse = {'detail':'Invalid Request'}
        return Response(stringResponse, status=status.HTTP_400_BAD_REQUEST)
    
class ProductoDetailView(generics.RetrieveAPIView):
    queryset           = Producto.objects.all()
    serializer_class   = ProductoSerializer

    def get(self, request, *args, **kwargs):     
        return super().get( request, *args, **kwargs)

class ProductoListView(generics.ListAPIView):
    queryset           = Producto.objects.all()
    serializer_class   = ProductoSerializer
    def get_queryset(self):
        return super().get_queryset()