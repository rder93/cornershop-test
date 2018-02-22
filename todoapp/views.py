# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User

from todoapp.serializers import *
from todoapp.models import *

from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status


# Create your views here.

class UserRegisterView(generics.ListCreateAPIView):
	"""
	User create & list view
	"""
	queryset = User.objects.all()
	serializer_class = UserRegisterSerializer


class ToDoListView(generics.ListCreateAPIView):
	"""
	Todo list and creating new tasks
	"""
	queryset = ToDoList.objects.all()
	serializer_class = ToDoListSerializer


class ToDoListCreateView(generics.CreateAPIView):
	"""
	ToDoList create view
	"""
	queryset = ToDoList.objects.all()
	serializer_class = ToDoListSerializer


class SubToDoListView(generics.ListCreateAPIView):
	"""
	Sub-Todo list and creating new sub-tasks
	"""
	queryset = SubToDoList.objects.all()
	serializer_class = SubToDoListSerializer


class SubToDoListCreateView(generics.ListCreateAPIView):
	"""
	SubToDoList create view
	"""
	queryset = SubToDoList.objects.all()
	serializer_class = SubToDoListSerializer


class TodoEditDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a todo instance.
    """
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer


class SubTodoEditDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a subtodo instance.
    """
    queryset = SubToDoList.objects.all()
    serializer_class = SubToDoListSerializer