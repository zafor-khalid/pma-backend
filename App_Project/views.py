from django.shortcuts import render
from .models import Project,Task,Activity
from .serializer import ProjectSerializer,TaskSerializer,ActivitySerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [
        IsAuthenticated,
    ]

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [
        IsAuthenticated,
    ]
