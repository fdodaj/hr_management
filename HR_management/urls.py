from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='app')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('app.user_api')),
    path('department/', include('app.department_url')),
    path('', schema_view),
]
