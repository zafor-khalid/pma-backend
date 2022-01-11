from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet,basename="user-list")

urlpatterns=[
   path('', include(router.urls)),
   # path('',views.ProjectListCreateView.as_view(),name='project-list'),
   # path('task/',views.TaskListCreateView.as_view(),name='task-list')

]