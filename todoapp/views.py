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


class TodoListView(generics.ListCreateAPIView):
	"""
	Todo list and creating new tasks
	"""
	queryset = TodoList.objects.all()
	serializer_class = TodoListSerializer


class SubTodoListView(generics.ListCreateAPIView):
	"""
	Sub-Todo list and creating new sub-tasks
	"""
	queryset = SubTodoList.objects.all()
	serializer_class = SubTodoListSerializer


class TodoEditDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a todo instance.
    """
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class SubTodoEditDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a subtodo instance.
    """
    queryset = SubTodoList.objects.all()
    serializer_class = SubTodoListSerializer