from django.urls import path
from . import views
from .views import ListUser , UpdateView,CreateUser, UserDetail, UserDestroyAPIView

urlpatterns = [
    path('', ListUser.as_view()),
    path('new/', CreateUser.as_view()),
    path('detail/<int:pk>', UserDetail.as_view()),
    path('update/<int:pk>', UpdateView.as_view()),
    path('delete/<int:pk>', UserDestroyAPIView.as_view())



]


