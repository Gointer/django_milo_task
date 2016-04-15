from django.test import TestCase
from django.core.urlresolvers import reverse


class MyUserListViewTest(TestCase):
	def test_item_list_renders_item_template(self):
		response = self.client.get(reverse('user-list'))
		self.assertTemplateUsed(response, 'user-list.html')

	def test_item_list_view_with_no_persons(self):
		response = self.client.get(reverse('user-list'))
		self.assertEqual(response.status_code,200)
		self.assertContains(response,"No user are available.")
		