from django.conf.urls import url
from todoapp.views import *

urlpatterns = [
	url(r'^create/user', CreateUserView.as_view(), name='create_user'),
    url(r'^todo/', ToDoListView.as_view(), name='todolist'),
    url(r'^subtodo/', SubToDoListView.as_view(), name='subtodolist'),
]