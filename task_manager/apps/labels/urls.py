from django.urls import path
from .views import (ListLabelView, CreateLabelView,
                    UpdateLabelView, DeleteLabelView)


urlpatterns = [
    path('', ListLabelView.as_view(), name='labels_index'),
    path('create/', CreateLabelView.as_view(), name='labels_create'),
    path('<int:pk>/update/', UpdateLabelView.as_view(), name='labels_update'),
    path('<int:pk>/delete/', DeleteLabelView.as_view(), name='labels_delete')
]
