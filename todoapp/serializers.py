from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth.models import User

from todoapp.models import *


class UserRegisterSerializer(serializers.ModelSerializer):
	"""
	Fields from user serializer and validate data received from view to create an account
	"""
	email = serializers.EmailField(required=True)
	username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
	password = serializers.CharField(min_length=5, style={'input_type': 'password'})

	def create(self, validated_data):
		user = User.objects.create_user(validated_data['username'], validated_data['email'],
			validated_data['password'])
		return user

	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'password')


class SubTodoSerializer(serializers.ModelSerializer):

	class Meta:
		model = SubTodo
		fields = ('id', 'subtask_name', 'status', 'todolist')
		depth = 1


class SubTodoEditSerializer(serializers.ModelSerializer):

	"""
    Fields from subtodo-list serializer and only can change status
    """
	class Meta:
		model = SubTodo
		fields = ('id', 'subtask_name', 'status', 'todolist')
		read_only_fields = ('subtask_name', 'todolist')
		depth = 1


class SubTodoCreateSerializer(serializers.ModelSerializer):

	"""
    Subtodo create view
    """
	class Meta:
		model = SubTodo
		fields = ('id', 'subtask_name', 'status', 'todolist')
		read_only_fields = ('status',)
		# depth = 1


class TodoSerializer(serializers.ModelSerializer):

	subtodolist = SubTodoSerializer(many=True, read_only=True)

	class Meta:
		model = Todo
		fields = ('id', 'task_name', 'status', 'subtodolist')


class TodoCreateSerializer(serializers.ModelSerializer):

	# subtodolist = SubTodoListSerializer(many=True, read_only=True)

	class Meta:
		model = Todo
		fields = ('id', 'task_name', 'status')
		read_only_fields = ('status',)


class TodoEditSerializer(serializers.ModelSerializer):
	"""
    Fields from todolist serializer and only can change status
    """
	class Meta:
		model = Todo
		fields = ('id', 'task_name', 'status', 'subtodolist')
		read_only_fields = ('task_name', 'subtodolist',)
		depth = 1

	"""
    Update all subtodo list status when todo status change
    """
	def update(self, instance, validated_data):
		Todo.objects.filter(pk=instance.pk).update(status=validated_data['status'])
		SubTodo.objects.filter(todolist=instance.pk).update(status=validated_data['status'])
		todo = Todo.objects.get(pk=instance.pk)
		return todo