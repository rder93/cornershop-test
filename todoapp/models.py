# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ToDoList(models.Model): 

	task_name = models.CharField(max_length=250, unique=True)
	status = models.BooleanField("Falta por hacer!", default=True)

	def __unicode__(self): 
		return self.task_name, self.status

	class Meta:
		ordering = ['task_name']


class SubToDoList(models.Model):
	todolist = models.ForeignKey(ToDoList)
	subtask_name = models.CharField(max_length=250, unique=True)
	status = models.BooleanField("Falta por hacer!", default=True)

	def __unicode__(self):
		return self.subtask_name, self.todolist, self.status