from rest_framework import serializers
from todoapp.models import *

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

	# def create(self, validated_data):
	# 	subtodolist_data = validated_data.pop('subtodolist')
	# 	# print(subtodolist_data)
	# 	todolist = ToDoList.objects.create(**validated_data)
	# 	SubToDoList.objects.create(todolist=todolist, **subtodolist_data)
	# 	return todolist