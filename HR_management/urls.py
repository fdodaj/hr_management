from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Hr Management')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('employee.urls')),
    path('department/', include('department.urls')),
    path('holiday/', include('holiday.urls')),
    path('permission/', include('permission.urls')),
    path('', schema_view),
    path('role/', include('role.urls'))
]
