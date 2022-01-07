from django.urls import path 
from . import views


urlpatterns=[
   
   path('',views.ProjectListCreateView.as_view(),name='project-list'),
   path('task/',views.TaskListCreateView.as_view(),name='task-list')

]