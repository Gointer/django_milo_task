import random

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


def rand_int():
    """
    Random Id
    """
    r = random.randint(0, 100)
    return r

class MyUser(AbstractUser):
	birthday = models.DateField()
	rand_int = models.IntegerField(default=rand_int)

	REQUIRED_FIELDS = ['birthday']

	def get_absolute_url(self):
		return reverse('user-detail', args=[self.pk])