from rest_framework import serializers
from api.models import BaseTrack
from api.models import User
from api.models import Collaboration

class CollaborationsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Collaboration
		fields = ('id', 'title', 'collaborators', 'date_created', 'date_modified')
		read_only_fields = ('date_created', 'date_modified')