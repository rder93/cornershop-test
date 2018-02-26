# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	"""
	Function to add automatically token to new user when register
	"""
	if created:
		Token.objects.create(user=instance)


class Todo(models.Model): 
	"""
	Fields from model
	"""
	CHOICE = [(False,'Falta por hacer!'),(True,'Resuelta tarea!')]
	task_name = models.CharField(max_length=250, unique=True)
	status = models.BooleanField(choices=CHOICE, default=False, blank=True)

	def __unicode__(self): 
		return '%s' % (self.task_name)

	"""
	Ordering by task_name the data
	"""
	class Meta:
		ordering = ['task_name']


class SubTodo(models.Model):
	"""
	Fields from model
	"""
	CHOICE = [(False,'Falta por hacer!'),(True,'Resuelta tarea!')]
	subtask_name = models.CharField(max_length=250, unique=True)
	status = models.BooleanField(choices=CHOICE, default=False)
	todolist = models.ForeignKey(Todo, related_name='subtodolist')

	def __unicode__(self):
		return '%s / SubTodo: %s' % (self.subtask_name, self.todolist)