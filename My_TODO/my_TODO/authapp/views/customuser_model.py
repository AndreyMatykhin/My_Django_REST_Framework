from rest_framework.viewsets import ModelViewSet
from authapp.models import CustomUser
from authapp.serializers import CustomUserModelSerializer


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer
