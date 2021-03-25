from django.urls import path
from . import views
from .views import UserDetail, UpdateView

urlpatterns = [
    path('', views.UserList.as_view()),
    path('user/<int:pk>', UserDetail.as_view()),
    path('<int:pk>', UpdateView.as_view()),

]


