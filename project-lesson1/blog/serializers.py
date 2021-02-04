from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name']

class PostSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Post
        exclude = []
        # depth = 1

