from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth.models import User

from todoapp.models import *

class UserSerializer(serializers.ModelSerializer):
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


class SubToDoListSerializer(serializers.ModelSerializer):

	# todolist = serializers.StringRelatedField(many=True)

	class Meta:
		model = SubToDoList
		fields = ('id', 'subtask_name', 'status', 'todolist')


class ToDoListSerializer(serializers.ModelSerializer):

	subtodolist = SubToDoListSerializer(many=True, read_only=True)

	class Meta:
		model = ToDoList
		fields = ('id', 'task_name', 'status', 'subtodolist')
		read_only_fields = ('status', )

	# def create(self, validated_data):
	# 	subtodolist_data = validated_data.pop('subtodolist')
	# 	# print(subtodolist_data)
	# 	todolist = ToDoList.objects.create(**validated_data)
	# 	SubToDoList.objects.create(todolist=todolist, **subtodolist_data)
	# 	return todolist