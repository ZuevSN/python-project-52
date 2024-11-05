from django.urls import path
from task_manager.statuses.views import (
    StatusListView,
    StatusCreateView,
    StatusUpdateView,
    StatusDeleteView
)

urlpatterns = [
    path('', StatusListView.as_view(), name='statuses'),
    path('create/', StatusCreateView.as_view(), name='create_status'),
    path('<int:pk>/edit/', StatusUpdateView.as_view(), name='edit_status'),
    path('<int:pk>/delete/', StatusDeleteView.as_view(), name='delete_status'),
]