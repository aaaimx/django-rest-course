from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import User, Division

class GroupSerializer(serializers.ModelSerializer):

    permissions = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='codename'
    )

    class Meta:
        model = Group
        # fields = ['name', 'id']
        exclude = []

class UserSerializer(serializers.ModelSerializer):

    groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    division = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = User
        exclude = ['password', 'user_permissions']

class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'birthdate', 'division']

class UserCreateSerializer(serializers.ModelSerializer):
    
    extra_kwargs = { 'password': {'write_only': True }}
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'birthdate', 'password', 'groups']

    def create(self, validated_data):
        groups = validated_data.pop('groups')
        user = User(**validated_data)
        user.set_password(validated_data.get('password'))
        division = self.context['request'].user.division
        user.division = division
        user.save()
        user.groups.set(groups)
        return user