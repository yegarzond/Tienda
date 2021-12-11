from rest_framework                            import status, views, generics
from rest_framework.response                   import Response
from rest_framework_simplejwt.serializers      import TokenObtainPairSerializer

from appTienda.models import User
from appTienda.serializers.userSerializer import UserSerializer


class UserCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserListView(generics.ListAPIView):
    queryset           = User.objects.all()
    serializer_class   = UserSerializer
    def get_queryset(self):
        return super().get_queryset()