from django.contrib.auth.models import Group
from user_manager.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'last_name' , 'first_name', 'date_of_birth', 'groups', 'gender']

class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password', 'date_of_birth', 'last_name', 'first_name', 'gender')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print("CREATING", validated_data)
        password = validated_data.pop('password')
        print(password)
        user = User.objects.create_user(
                **validated_data,
        )
        user.set_password(password)
        user.save()
        return user

