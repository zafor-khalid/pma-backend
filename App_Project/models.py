from django.db import models

# Create your models here.
class Project(models.Model):
    project_title = models.CharField(max_length = 5550)
    project_description = models.CharField(max_length = 5550)

    def __str__(self):
        return self.project_title

class Task(models.Model):
    project_title = models.CharField(max_length = 5550)
    project_description = models.CharField(max_length = 5550)