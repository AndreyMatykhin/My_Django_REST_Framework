from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from authapp.models.custom_user import CustomUser


class CustomUserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['url',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'user_category',
                  'is_active',
                  'date_joined',
                  ]


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
