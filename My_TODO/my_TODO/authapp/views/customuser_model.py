from rest_framework.viewsets import ModelViewSet
from authapp.models import CustomUser
from authapp.serializers import CustomUserModelSerializer, CustomUserSerializer
from rest_framework import mixins, viewsets


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return CustomUserSerializer
        return CustomUserModelSerializer


class UserViewSet(mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
