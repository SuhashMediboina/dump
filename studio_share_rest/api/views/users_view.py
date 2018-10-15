from django.shortcuts import render
from rest_framework import viewsets
from api.models import User
from api.serializers import UsersSerializer

class UsersView(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UsersSerializer