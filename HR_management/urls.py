from django.contrib import admin
from django.urls import path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view)
]
