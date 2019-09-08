from rest_framework import serializers
from .models import Note, TaskGroup, Task

class NoteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Note
		fields = ('id', 'title', 'text', 'color', 'column', 'created_date', 'item_type')

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ('id', 'text', 'sno', 'task_group')

class TaskGroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = TaskGroup
		fields = ('id', 'title', 'color', 'column', 'created_date', 'item_type')

class TaskGroupSerializer2(serializers.ModelSerializer):
	tasks = serializers.SerializerMethodField('get_tasks')

	class Meta:
		model = TaskGroup
		fields = ('id', 'title', 'color', 'column', 'tasks', 'created_date', 'item_type')

	def get_tasks(self, instance):
		tasks = instance.tasks.all().order_by('sno')
		return TaskSerializer(tasks, many=True).data
