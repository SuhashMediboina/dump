from django.test import TestCase
from .models import Post

# Create your tests here.
class PostTestCase(TestCase):
	def setUp(self):
		self.message = "This is an awesome first message test"
		self.post = Post(message = self.message)

	def test_model_can_create_a_post(self):
		old_count = Post.objects.count()
		self.post.save()
		new_count = Post.objects.count()
		self.assertNotEqual(old_count, new_count)
