from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views
# from .views import

urlpatterns = [
    path('', views.CreateRole.as_view()), # create holiday
    path('<int:pk>', views.RoleDetail.as_view()), # get holiday by ID
    path('update/<int:pk>', views.UpdateRole.as_view()), # update holiday
    path('all', views.RoleList.as_view()), # get holiday list
    # path('delete/<int:pk>', views.HolidayDestroyAPIView.as_view()), # delete holiday by ID
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]

