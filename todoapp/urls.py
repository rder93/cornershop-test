from django.conf.urls import url

from rest_framework.authtoken import views

from todoapp.views import *

urlpatterns = [
	url(r'^login/$', views.obtain_auth_token),
	url(r'^register/', UserRegisterView.as_view(), name='register'),
    url(r'^todo/$', TodoListView.as_view(), name='todo'),
    url(r'^todo/create/$', TodoCreateView.as_view(), name='todo_create'),
    url(r'^todo/(?P<pk>\d+)/$', TodoEditDetail.as_view(), name='todo_edit'),
    url(r'^subtodo/$', SubTodoListView.as_view(), name='subtodo'),
    url(r'^subtodo/create/$', SubTodoCreateView.as_view(), name='subtodo_create'),
    url(r'^subtodo/(?P<pk>\d+)/$', SubTodoEditDetail.as_view(), name='subtodo_edit'),
]
