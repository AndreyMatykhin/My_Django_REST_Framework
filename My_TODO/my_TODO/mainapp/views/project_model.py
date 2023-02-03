from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from mainapp.models import Project
from mainapp.serializers import ProjectSerializer, ProjectSerializerBase
from django_filters import rest_framework as filters
from mainapp.filters import ProjectFilter


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectLimitOffsetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProjectFilter

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ProjectSerializer
        return ProjectSerializerBase
