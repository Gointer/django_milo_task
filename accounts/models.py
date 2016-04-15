import random

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
	birthday = models.DateField()
	rand_int = models.IntegerField(default=random.randint(1,100))

	REQUIRED_FIELDS = ['birthday']

	def get_absolute_url(self):
		return reverse('user-detail', args=[self.pk])