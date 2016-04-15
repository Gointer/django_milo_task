from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.http import HttpResponse

from .app.admin import UserResource
from .models import MyUser


def export_excel(request):
	dataset = UserResource().export()
	response = HttpResponse(dataset.csv, content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=list.csv'
	return response

class MyUserListView(ListView):
	model = MyUser
	template_name = 'user-list.html'


class MyUserCreate(CreateView):
	model = MyUser
	fields = ['username', 'birthday']
	template_name = 'user-create.html'


class MyUserDetailView(DetailView):
	model = MyUser
	template_name = 'user-detail.html'


class MyUserUpdate(UpdateView):
	model = MyUser
	fields = ['username', 'birthday']
	template_name = 'user-create.html'


class MyUserDelete(DeleteView):
	model = MyUser
	template_name = 'user-delete.html'
	success_url = reverse_lazy('user-list')