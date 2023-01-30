from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from authapp.models.custom_user import CustomUser


class CustomUserModelSerializer(HyperlinkedModelSerializer):
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
        return CustomUser.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        super().update(instance, validated_data)
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        super().update(instance, validated_data)
        instance.set_password(validated_data['password'])
        instance.save()
        return instance
