from rest_framework import serializers
from .models import Project,Task


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ["id"]
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ["id"]