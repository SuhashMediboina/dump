from django.shortcuts import render
from rest_framework import viewsets
from api.models import BaseTrack
from api.serializers import BaseTracksSerializer

class BaseTracksView(viewsets.ModelViewSet):
  queryset = BaseTrack.objects.all()
  serializer_class = BaseTracksSerializer