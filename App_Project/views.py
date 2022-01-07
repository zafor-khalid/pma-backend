from django.shortcuts import render
from .models import Project,Task
from .serializer import ProjectSerializer,TaskSerializer
from rest_framework import generics
# Create your views here.

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
