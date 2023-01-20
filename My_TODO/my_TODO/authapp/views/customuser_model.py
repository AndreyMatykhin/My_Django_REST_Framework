from rest_framework.viewsets import ModelViewSet
from authapp.models import CustomUser
from authapp.serializers import CustomUserModelSerializer, CustomUserSerializer
from rest_framework import mixins, viewsets
from rest_framework.renderers import AdminRenderer


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserModelSerializer


class UserViewSet(mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
