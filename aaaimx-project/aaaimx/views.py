from django.shortcuts import render
from rest_framework import viewsets, generics
from django.contrib.auth.models import Group

from .serializers import GroupSerializer, UserSerializer, UserInfoSerializer, UserCreateSerializer
from .models import User, Division
from .permissions import UserPermission

# Create your views here.
class GroupView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    http_method_names = ['get', 'post', 'patch', 'delete']

    permission_classes = (UserPermission,)

    filterset_fields = []
    search_fields = ['username', 'email']
    ordering_fields = ['id', 'email', 'birthdate', 'username']
    ordering = ['-date_joined']

    def get_queryset(self):
        division = self.request.user.division
        return User.objects.filter(division=division)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserInfoSerializer
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer

