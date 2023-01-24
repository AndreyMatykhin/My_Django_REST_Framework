from rest_framework import serializers
from mainapp.models import TODO
from mainapp.serializers import ProjectSerializer


class TODOSerializer(serializers.HyperlinkedModelSerializer):
    users_list = serializers.StringRelatedField(many=True)
    project_name = serializers.SlugRelatedField(read_only=True, slug_field='project_name')

    class Meta:
        model = TODO
        fields = '__all__'
