from rest_framework import serializers
from api.models import BaseTrack
from api.models import User

class BaseTracksSerializer(serializers.ModelSerializer):

	class Meta:
		model = BaseTrack
		fields = ('id', 'author', 'name', 'date_created', 'date_modified')
		read_only_fields = ('date_created', 'date_modified')