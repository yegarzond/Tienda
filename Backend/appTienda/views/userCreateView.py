from rest_framework import status, views
from rest_framework.response import Response

class UserCreateViews(views.APIView):
    def post(self, request, *args, **kwargs):

        return Response('hola', status = status.HTTP_200_OK)
        print('Prueba')
