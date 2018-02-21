# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User

from todoapp.serializers import *
from todoapp.models import *

from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from django.contrib.auth.models import User


# Create your views here.

class CreateUserView(generics.ListCreateAPIView):

	"""
	User create & list view
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer


class ToDoListView(generics.ListCreateAPIView):

	"""
	ToDoList create & list view
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
	SubToDoList view
	"""
	queryset = SubToDoList.objects.all()
	serializer_class = SubToDoListSerializer


class SubToDoListCreateView(generics.ListCreateAPIView):

	"""
	SubToDoList create view
	"""
	queryset = SubToDoList.objects.all()
	serializer_class = SubToDoListSerializer