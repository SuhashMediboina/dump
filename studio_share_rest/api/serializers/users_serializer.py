from rest_framework import serializers
from api.models import User

class UsersSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('id', 'name', 'date_created', 'date_modified')
		read_only_fields = ('date_created', 'date_modified')