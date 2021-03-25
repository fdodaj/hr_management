from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.DepartmentList.as_view()),
    path('user/<int:pk>', views.DepartmentDetail.as_view()),
    path('<int:pk>', views.UpdateDepartment.as_view()),

]


