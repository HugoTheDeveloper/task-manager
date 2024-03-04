from django.urls import path
from .views import (ListStatusView, CreateStatusView,
                    UpdateStatusView, DeleteStatusView)


urlpatterns = [
    path('', ListStatusView.as_view(), name='status_index'),
    path('create/', CreateStatusView.as_view(), name='status_create'),
    path('<int:pk>/update/', UpdateStatusView.as_view(), name='status_update'),
    path('<int:pk>/delete/', DeleteStatusView.as_view(), name='status_delete')
]
