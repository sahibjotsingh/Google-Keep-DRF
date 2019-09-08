# demo/api.py
from rest_framework.routers import DefaultRouter
from api.views import TaskGroupViewSet, TaskGroupViewSet2, TaskViewSet, NoteViewSet
from rest_framework_extensions.routers import NestedRouterMixin
  
router = DefaultRouter()
 

class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass

router = NestedDefaultRouter()

router.register('notes', NoteViewSet, basename='notes') 
router.register('tasks', TaskViewSet, basename='tasks')
router.register('task-group-tasks', TaskGroupViewSet2, basename='task_group_tasks')

task_groups_router = router.register('task-groups', TaskGroupViewSet)
task_groups_router.register('tasks',TaskViewSet,basename='group-tasks',parents_query_lookups=['task_group'])

