from django.urls import path
from task_manager.users.views import (
    UserListView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView
)

urlpatterns = [
    path('', UserListView.as_view(), name='users'),
    path('create/', UserCreateView.as_view(), name='create_user'),
    path('<int:pk>/edit/', UserUpdateView.as_view(), name='edit_user'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete_user'),
]
