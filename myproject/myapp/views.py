from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import permissions


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    http_method_names = ['get','post','post','delete']

# POST COMMENT POST_TYPE FOLLOW

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
  
    def create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    http_method_names = ['get','post','post','delete']


class PostTypeViewSet(ModelViewSet):
    queryset = PostType.objects.all()
    serializer_class = PostTypeSerializer
    http_method_names = ['get','post','post','delete']


class FollowViewSet(ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    http_method_names = ['get','post','post','delete']


class ReadOnlyViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = ReadOnlySerializer
    http_method_names = ['get']

