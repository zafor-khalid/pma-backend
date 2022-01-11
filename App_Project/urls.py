from django.urls import path,include
from . import views
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'project', views.ProjectViewSet)
router.register(r'task', views.TaskViewSet,basename="task-list")
# router.register(r'activity', views.ActivityViewSet)

urlpatterns=[
   path('', include(router.urls)),
   # path('',views.ProjectListCreateView.as_view(),name='project-list'),
   # path('task/',views.TaskListCreateView.as_view(),name='task-list')

]