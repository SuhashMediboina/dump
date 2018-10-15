from django.db import models
from .user import User

# Create your models here.
class Post(models.Model):
	message = models.CharField(max_length = 500, blank = False)
	author = models.ForeignKey(User, null = True, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add = True)
	date_modified = models.DateTimeField(auto_now = True)

	def __str__(self):
		return (self.message, self.author)
