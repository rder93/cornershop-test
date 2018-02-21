# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User

from todoapp.serializers import *
from todoapp.models import *

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


# Create your views here.

class ToDoListView(generics.ListAPIView):

	"""
	ToDoList view
	"""
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer


class ToDoListCreateView(generics.CreateAPIView):

	"""
	ToDoList create view
	"""
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer


class SubToDoListView(generics.ListAPIView):

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