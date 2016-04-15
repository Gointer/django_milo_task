import datetime 

from django.test import TestCase

from ..models import MyUser


class MyUserModelTest(TestCase):
	def setUp(self):
		self.my_user = MyUser.objects.create(
			username='user',
			birthday=datetime.date.today(),
		)

	def test_create_rand_int_in_range(self):
		self.assertTrue(1 <= self.my_user.rand_int <= 100)

	def tearDown(self):
		self.my_user.delete()

