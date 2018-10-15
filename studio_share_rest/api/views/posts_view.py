from django.shortcuts import render
from rest_framework import viewsets
from api.models import Post
from api.serializers import PostsSerializer

class PostsView(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostsSerializer