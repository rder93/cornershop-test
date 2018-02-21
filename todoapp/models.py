# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ToDoList(models.Model): 

	CHOICE = [(0,'Falta por hacer!'),(1,'Resuelta tarea!')]
	task_name = models.CharField(max_length=250, unique=True)
	status = models.BooleanField(choices=CHOICE, default=0, blank=True)

	def __unicode__(self): 
		return '%s %s' % (self.task_name)

	class Meta:
		ordering = ['task_name']


class SubToDoList(models.Model):

	CHOICE = [(0,'Falta por hacer!'),(1,'Resuelta tarea!')]
	subtask_name = models.CharField(max_length=250, unique=True)
	status = models.BooleanField(choices=CHOICE, default=0)
	todolist = models.ForeignKey(ToDoList, related_name='subtodolist')

	def __unicode__(self):
		return '%s %s  %s' % (self.subtask_name, self.todolist)