from django.contrib import admin
from .models import User, Department, Role, Holiday, Permission


admin.site.register(User)
admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Holiday)
admin.site.register(Permission)
