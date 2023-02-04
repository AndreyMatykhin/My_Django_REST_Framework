from rest_framework import serializers
from mainapp.models import Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    users_list = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectSerializerBase(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
