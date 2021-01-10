from django.urls import path

from .views import *

urlpatterns = [
    path('task/create', TaskCreateView.as_view()),
    path('task/list', TaskListView.as_view()),
    path('task/edit/<int:pk>', TaskDetailView.as_view()),
]
