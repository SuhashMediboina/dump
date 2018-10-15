from django.db import models
from .user import User
from .base_track import BaseTrack

# Create your models here.
class Collaboration(models.Model):
	title = models.CharField(max_length = 500, blank = False)
	collaborators = models.ManyToManyField(User)
	date_created = models.DateTimeField(auto_now_add = True)
	date_modified = models.DateTimeField(auto_now = True)

	def __str__(self):
		return (self.title, self.author, self.collaborators)
