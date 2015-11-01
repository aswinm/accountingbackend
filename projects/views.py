from django.shortcuts import render
from projects.models import Project,TimeDuration
from rest_framework import viewsets
from projects.serializers import ProjectSerializer,TimeDurationSerializer

class ProjectViewSet(viewsets.ModelViewSet):
        queryset = Project.objects.all()
        serializer_class = ProjectSerializer

class TimeDurationViewSet(viewsets.ModelViewSet):
        queryset = TimeDuration.objects.all()
        serializer_class = TimeDurationSerializer
# Create your views here.
