from rest_framework.viewsets import ModelViewSet
from mainapp.models import Project
from mainapp.serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
