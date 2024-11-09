from django.urls import path
from task_manager.labels.views import (
    LabelListView,
    LabelCreateView,
    LabelUpdateView,
    LabelDeleteView,
)
from .models import Label

urlpatterns = [
    path('', LabelListView.as_view(), name='labels'),
    path('create/', LabelCreateView.as_view(), name='create_label'),
    path('<int:pk>/edit/', LabelUpdateView.as_view(), name='edit_label'),
    path('<int:pk>/delete/', LabelDeleteView.as_view(), name='delete_label'),
]