from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer, CharField
from authapp.models.custom_user import CustomUser


class CustomUserModelSerializer(HyperlinkedModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['url',
                  'username',
                  'email',
                  'user_category',
                  'is_active',
                  'date_joined',
                  'password'
                  ]

    def create(self, validated_data):
        user = super(CustomUserModelSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class CustomUserSerializer(ModelSerializer):
     class Meta:
        model = CustomUser
        fields = '__all__'
