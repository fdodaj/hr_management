from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('create', views.CreateHoliday.as_view()), # create holiday
    path('<int:pk>', views.HolidayDetail.as_view()), # get holiday by ID
    path('update/<int:pk>', views.UpdateHoliday.as_view()), # update holiday
    path('', views.HolidayList.as_view()), # get holiday list
    path('delete/<int:pk>', views.HolidayDestroyAPIView.as_view()), # delete holiday by ID
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]
