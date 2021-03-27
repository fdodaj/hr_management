from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('crete', views.CreateHoliday.as_view()),
    path('holiday/<int:pk>', views.HolidayDetail.as_view()),
    path('<int:pk>', views.UpdateHoliday.as_view()),
    path('all', views.HolidayList.as_view()),
    path('delete/<int:pk>', views.HoldayDestroyAPIView.as_view())

]
