from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Post, User
from .serializers import PostSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
       
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filterset_fields = ['title', 'user']
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'created_at']
    ordering = ['-created_at']

    # def get_serializer_class(self):
    #     pass

    # def get_queryset(self):
    #     pass

    def retrieve(self, request, *args, **kwargs):
        instance = Post.objects.get(pk=kwargs['pk'])
        serializer = PostSerializer(instance) 
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_200_OK)


