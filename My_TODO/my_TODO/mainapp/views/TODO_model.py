from rest_framework.viewsets import ModelViewSet
from mainapp.models import TODO
from mainapp.serializers import TODOSerializer


class TODOViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer
