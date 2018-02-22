from django.conf.urls import url

from rest_framework.authtoken import views

from todoapp.views import *

urlpatterns = [
	url(r'^login/$', views.obtain_auth_token),
	url(r'^register/', UserRegisterView.as_view(), name='create_user'),
    url(r'^todo/$', ToDoListView.as_view(), name='todolist'),
    url(r'^subtodo/$', SubToDoListView.as_view(), name='subtodolist'),
    url(r'^todo/(?P<pk>\d+)/$', TodoEditDetail.as_view(), name='todo_edit'),
    url(r'^subtodo/(?P<pk>\d+)/$', SubTodoEditDetail.as_view(), name='subtodo_edit'),
]
