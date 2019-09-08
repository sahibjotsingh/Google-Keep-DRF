from django.contrib import admin
from .models import Note, TaskGroup, Task

admin.site.register(Note)
admin.site.register(TaskGroup)
admin.site.register(Task)

