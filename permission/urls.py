from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.ListPermission.as_view()),
    path('create/', views.CreatePermission.as_view()),
    path('permision/<int:pk>', views.PermissionDetail.as_view()),
    path('<int:pk>', views.UpdatePermission.as_view()),
    path('delete/<int:pk>', views.PermissionDestroyAPIView.as_view())

]
