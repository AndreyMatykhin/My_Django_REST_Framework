from django_filters import rest_framework as filters
from mainapp.models import Project, TODO


class ProjectFilter(filters.FilterSet):
    project_name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['project_name']


class TODOFilter(filters.FilterSet):
    project_name__project_name = filters.CharFilter(label='Project name contains', lookup_expr='contains')


    class Meta:
        model = TODO
        fields = {'created': ('gte', 'lte')}

