from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='users_index'),
    path('create/', views.CreateUserView.as_view(), name='users_create'),
    path('<int:pk>/update/', views.UpdateUserView.as_view(),
         name='users_update'),
    path('<int:pk>/delete/', views.DeleteUserView.as_view(),
         name='users_delete')
]
