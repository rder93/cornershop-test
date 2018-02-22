from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth.models import User

from todoapp.models import *


class UserRegisterSerializer(serializers.ModelSerializer):

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


class SubTodoListSerializer(serializers.ModelSerializer):

	class Meta:
		model = SubTodoList
		fields = ('id', 'subtask_name', 'status', 'todolist')


class TodoListSerializer(serializers.ModelSerializer):

	subtodolist = SubTodoListSerializer(many=True, read_only=True)

	class Meta:
		model = TodoList
		fields = ('id', 'task_name', 'status', 'subtodolist')