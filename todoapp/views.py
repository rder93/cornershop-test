# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status

from todoapp.serializers import *
from todoapp.models import *

# Create your views here.

class UserRegisterView(generics.ListCreateAPIView):
	"""
	User create & list view
	"""
	queryset = User.objects.all()
	serializer_class = UserRegisterSerializer


class TodoListView(generics.ListAPIView):
	"""
	Todo list view
	"""
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer


class TodoCreateView(generics.CreateAPIView):
	"""
	Todo create view
	"""
	queryset = Todo.objects.all()
	serializer_class = TodoCreateSerializer


class TodoEditDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a todo instance.
    """
    queryset = Todo.objects.all()
    serializer_class = TodoEditSerializer


class SubTodoListView(generics.ListAPIView):
	"""
	Sub-tasks from Todo List
	"""
	queryset = SubTodo.objects.all()
	serializer_class = SubTodoSerializer


class SubTodoCreateView(generics.CreateAPIView):
	"""
	Todo create view
	"""
	queryset = SubTodo.objects.all()
	serializer_class = SubTodoCreateSerializer


class SubTodoEditDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a subtodo instance.
    """
    queryset = SubTodo.objects.all()
    serializer_class = SubTodoEditSerializer