# demo/api.py
from rest_framework.routers import DefaultRouter
from api.views import TaskGroupViewSet, TaskViewSet, NoteViewSet, CombineListView
from rest_framework_extensions.routers import NestedRouterMixin
  
router = DefaultRouter()
 
router.register('task-groups', TaskGroupViewSet)
router.register('tasks', TaskViewSet)
router.register('notes', NoteViewSet)

class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass

router = NestedDefaultRouter()

notes_router = router.register('notes', NoteViewSet) 
task_groups_router = router.register('task-groups', TaskGroupViewSet)
task_groups_router.register('tasks',TaskViewSet,basename='group-tasks',parents_query_lookups=['task_group'])

