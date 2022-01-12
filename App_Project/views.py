from django.shortcuts import render
from .models import Project,Task
from .serializer import ProjectSerializer,TaskSerializer
from rest_framework import viewsets,generics
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    
class TaskViewSet(viewsets.ModelViewSet):
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    def get_queryset(self):
        queryset = Task.objects.all()
        project_id =self.request.query_params.get('project_id',None)
        task_id=self.request.query_params.get('task_id',None)
        print(project_id,task_id)
        if project_id is not None:
            print("project true")
            queryset=Task.objects.filter(project_title_id=project_id)
        if project_id and task_id is not None:
            print("task true")
            queryset=Task.objects.filter(project_title_id=project_id).filter(id=task_id)
        # print(queryset)
        return queryset

    
class TaskUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    def get_queryset(self):
        queryset = Task.objects.all()
        project_id =self.request.query_params.get('project_id',None)
        task_id=self.request.query_params.get('task_id',None)
        print(project_id,task_id)
        if project_id and task_id is not None:
            print("task true")
            queryset=Task.objects.filter(project_title_id=project_id).filter(id=task_id)
        # print(queryset)
        return queryset
# class ActivityViewSet(viewsets.ModelViewSet):
#     queryset = Activity.objects.all()
#     serializer_class = ActivitySerializer
#     # permission_classes = [
#     #     IsAuthenticated,
#     # ]
