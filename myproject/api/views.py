from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, viewsets, mixins
from rest_framework_extensions import mixins
from rest_framework.response import Response

class CombineListView(viewsets.ModelViewSet):
    serializer_class_Note = NoteSerializer
    serializer_class_TaskGroup = TaskGroupSerializer2

    def get_queryset_Note(self):
        return Note.objects.all().order_by('created_date')
    def get_queryset_TaskGroup(self):
        return TaskGroup.objects.all().order_by('created_date')

    def list(self, request, *args, **kwargs):
        notes = self.serializer_class_Note(self.get_queryset_Note(), many=True)
        task_groups = self.serializer_class_TaskGroup(self.get_queryset_TaskGroup(), many=True)
        return Response({
            "notes": notes.data,
            "task_groups": task_groups.data
        })

class TaskGroupRetrieveView(generics.RetrieveAPIView):
    serializer_class =  TaskGroupSerializer2
    queryset =  TaskGroup.objects.all()

class NoteViewSet(viewsets.ModelViewSet):
	serializer_class =  NoteSerializer
	queryset =  Note.objects.all()

class TaskGroupViewSet(mixins.NestedViewSetMixin, viewsets.ModelViewSet):
	serializer_class = TaskGroupSerializer
	queryset = TaskGroup.objects.all()
 
class TaskViewSet(mixins.NestedViewSetMixin, viewsets.ModelViewSet):
	serializer_class = TaskSerializer
	queryset = Task.objects.all().order_by('sno')



