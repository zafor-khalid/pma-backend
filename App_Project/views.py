from django.shortcuts import render
from .models import Project,Task
from .serializer import ProjectSerializer,TaskSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = [
    #     IsAuthenticated,
    # ]
    
class TaskViewSet(viewsets.ModelViewSet):
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = [
    #     IsAuthenticated,
    # ]
    def get_queryset(self):
        queryset = Task.objects.all()
        project_id =self.request.query_params.get('project_id',None)
        if project_id is not None:
            queryset=Task.objects.filter(project_title_id=project_id)
        return queryset

class TaskViewSet(viewsets.ModelViewSet):
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = [
    #     IsAuthenticated,
    # ]
    def get_queryset(self):
        queryset = Task.objects.all()
        project_id =self.request.query_params.get('project_id',None)
        if project_id is not None:
            queryset=Task.objects.filter(project_title_id=project_id)
        return queryset

# class ActivityViewSet(viewsets.ModelViewSet):
#     queryset = Activity.objects.all()
#     serializer_class = ActivitySerializer
#     # permission_classes = [
#     #     IsAuthenticated,
#     # ]
