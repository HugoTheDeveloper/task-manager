from django.urls import path
from .views import (TaskListView, TaskCreateView,
                    TaskDetailView, TaskUpdateView,
                    TaskDeleteView)


urlpatterns = [
    path('', TaskListView.as_view(), name='tasks_index'),
    path('<int:pk>/', TaskDetailView.as_view(), name='tasks_detail'),
    path('create/', TaskCreateView.as_view(), name='tasks_create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='tasks_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='tasks_delete')
]
