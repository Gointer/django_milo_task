import datetime

from django import template

from ..models import MyUser

register = template.Library()

@register.filter(name='eligible')
def eligible(value):
	today = datetime.date.today()
	timedelta = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
	if timedelta > 13:
		return 'allowed'
	else:
		return 'blocked'


@register.filter(name='bizzfuzz')
def bizzfuzz(value):
	if (value % 3 == 0) and (value % 5 == 0):
		return 'BizzFuzz'
	elif value % 3 == 0:
		return 'Bizz'
	elif value % 5 == 0:
		return 'Fuzz'
	else:
		return value