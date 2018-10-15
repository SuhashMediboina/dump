from django.shortcuts import render
from rest_framework import viewsets
from api.models import Collaboration
from api.serializers import CollaborationsSerializer

class CollaborationsView(viewsets.ModelViewSet):
  queryset = Collaboration.objects.all()
  serializer_class = CollaborationsSerializer