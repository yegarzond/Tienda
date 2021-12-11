from django.db.models import query
from django.utils import translation
from django.utils.translation import deactivate_all
from django.views import generic
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from appTienda.models.itemsFactura import ItemsFactura
from appTienda.serializers.itemsFacturaSerializer import ItemsFacturaSerializer
from appTienda.serializers.facturaSerializer import FacturaSerializer

class CreateFacturaView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer=FacturaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        