from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, viewsets, mixins
from rest_framework_extensions import mixins
from rest_framework.response import Response
from django.db.models import Q

class TaskGroupViewSet2(viewsets.ModelViewSet):
    serializer_class =  TaskGroupSerializer2

    def get_queryset(self):
        queryset =  TaskGroup.objects.all()
        search_text = self.request.query_params.get('search_text', None)
        if search_text is not None:
            queryset = queryset.filter(title__contains=search_text)
        return queryset

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class =  NoteSerializer

    def get_queryset(self):
        queryset =  Note.objects.all()
        search_text = self.request.query_params.get('search_text', None)
        if search_text is not None:
            queryset = queryset.filter(
                Q(title__contains=search_text) | 
                Q(text__contains=search_text)
            )
        return queryset

class TaskGroupViewSet(mixins.NestedViewSetMixin, viewsets.ModelViewSet):
	serializer_class = TaskGroupSerializer
	queryset = TaskGroup.objects.all()
 
class TaskViewSet(mixins.NestedViewSetMixin, viewsets.ModelViewSet):
	serializer_class = TaskSerializer
	queryset = Task.objects.all().order_by('sno')



