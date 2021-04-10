from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import ListUser, UpdateView, CreateUser, UserDetail, UserDestroyAPIView, UserPasswordView, Login, Logout
#    ,UpdatePasswordView

urlpatterns = [
    path('all', ListUser.as_view()),
    path('register', CreateUser.as_view()),
    # path('login', obtain_auth_token, name='api_token_auth'),
    path('<int:pk>', UserDetail.as_view()),
    path('update/<int:pk>', UpdateView.as_view()),
    path('delete/<int:pk>', UserDestroyAPIView.as_view()),
    path('password/<int:pk>', UserPasswordView.as_view()),
    path('login/', Login.as_view(), name='login'),
    path('logout11/', Logout.as_view(), name='logout'),


    # path('update-pass/<int:pk>', UpdatePasswordView.as_view()),
    # path('obtain-token', obtain_auth_token, name='api_token_auth')
]
