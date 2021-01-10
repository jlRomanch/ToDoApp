from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from .serializer import TaskDetailSerializer, TaskListSerializer
from .models import Task


class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskDetailSerializer


class TaskListView(generics.ListAPIView):
    serializer_class = TaskListSerializer
    queryset = Task.objects.all()
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, *args, **kwargs):
        return Response({"Tasks": self.queryset}, template_name='index.html')


class TaskDetailView(generics.RetrieveAPIView):
    serializer_class = TaskDetailSerializer
    queryset = Task.objects.all()
