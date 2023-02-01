from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from mainapp.models import TODO
from mainapp.serializers import TODOSerializer
from rest_framework import permissions
from django_filters import rest_framework as filters
from mainapp.filters import TODOFilter


class TODOLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class TODOViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer
    pagination_class = TODOLimitOffsetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TODOFilter

    def perform_destroy(self, instance):
        instance.complete()
