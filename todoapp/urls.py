from django.conf.urls import url
from todoapp.views import *

urlpatterns = [
    url(r'^todo/', ToDoListView.as_view(), name='toDolist'),
]