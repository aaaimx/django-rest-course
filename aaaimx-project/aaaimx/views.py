from django.shortcuts import render
from rest_framework import viewsets, generics
from django.contrib.auth.models import Group

from .serializers import GroupSerializer, UserSerializer
from .models import User, Division

# Create your views here.

class GroupView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer