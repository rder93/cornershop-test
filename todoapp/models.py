# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ToDoList(models.Model): 

	task_name = models.CharField(max_length=250, unique=True)
	status = models.BooleanField(default=True)

	def __unicode__(self): 
		return '%s: %s' % (self.task_name, self.status)

	class Meta:
		ordering = ['task_name']


class SubToDoList(models.Model):

	subtask_name = models.CharField(max_length=250, unique=True)
	status = models.BooleanField(default=True)
	todolist = models.ForeignKey(ToDoList, related_name='subtodolist')

	def __unicode__(self):
		return '%s: %s  %s' % (self.subtask_name, self.status, self.todolist)