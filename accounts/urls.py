from django.conf.urls import url

from .views import MyUserListView, MyUserCreate, MyUserDetailView, MyUserUpdate, MyUserDelete, export_excel

urlpatterns = [
    url(r'^$', MyUserListView.as_view(), name='user-list'),
    url(r'^new$', MyUserCreate.as_view(), name='user-create'),
    url(r'^(?P<pk>[-\w]+)/$', MyUserDetailView.as_view(), name='user-detail'),
    url(r'^export$', export_excel, name='export_excel'),
    url(r'^change/(?P<pk>[-\w]+)/$', MyUserUpdate.as_view(), name='user-change'),
    url(r'^delete/(?P<pk>[-\w]+)/$', MyUserDelete.as_view(), name='user-delete'),
]