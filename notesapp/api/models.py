from django.db import models
from django.utils.timezone import now

class Note(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField(max_length=1000)
	color = models.CharField(max_length=30, default='#ffffff')
	column = models.IntegerField(default=1)
	created_date = models.DateTimeField(default=now, editable=False)
	item_type = models.CharField(max_length=4, default='note', editable=False)

	def __str__(self):
		return '%s ' % self.title 

#, editable=False

class TaskGroup(models.Model):
	title = models.CharField(max_length=100)
	color = models.CharField(max_length=30, default='#ffffff')
	column = models.IntegerField(default=1)
	created_date = models.DateTimeField(default=now, editable=False)
	sno = models.IntegerField(default=0)
	item_type = models.CharField(max_length=9, default='task_list', editable=False)

	def __str__(self):
		return '%s ' % self.title

class Task(models.Model):
	text = models.TextField(max_length=1000, default='')
	sno = models.IntegerField(default=0)
	task_group = models.ForeignKey(TaskGroup, related_name='tasks', on_delete=models.CASCADE)

