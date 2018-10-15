from rest_framework import serializers
from api.models import Post

class PostsSerializer(serializers.ModelSerializer):

	class Meta:
		model = Post
		fields = ('id', 'author', 'message', 'date_created', 'date_modified')
		read_only_fields = ('date_created', 'date_modified')