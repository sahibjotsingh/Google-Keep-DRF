from django.conf.urls import url, include
from django.contrib import admin
from .api import router
from api import views
 
urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^api/combined/', views.CombineListView.as_view({'get': 'list'})),
	url(r'^api/task-group-tasks/(?P<pk>\d+)/$', views.TaskGroupRetrieveView.as_view()),
	url(r'^api/', include(router.urls))
]

