from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.ListRequest.as_view()),
    path('create', views.CreateRequest.as_view()),
    path('<int:pk>', views.RequestDetail.as_view()),
    path('update/<int:pk>', views.UpdateRequest.as_view()),
    path('<int:pk>', views.RequestDestroyAPIView.as_view()),
    # path('pto/<int:pk>', views.GetPto.as_view())
]
