from django.urls import path
from task_manager.statuses.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)
from .models import Task

urlpatterns = [
    path('', TaskListView.as_view(), name='tasks'),
#    path('', UniversalListView.as_view(model=Status), name='statuses'),
    path('create/', TaskCreateView.as_view(), name='create_task'),
    path('<int:pk>/edit/', TaskUpdateView.as_view(), name='edit_task'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='delete_task'),
]