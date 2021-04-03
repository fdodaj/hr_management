from django.db import models
from django.contrib.auth.models import User, AbstractUser
# from role.models import
from role.models import Role
from department.models import Department


class Employee(AbstractUser):
    department = models.ForeignKey(Department, on_delete=models.CASCADE,blank=True, null=True)
    # employee_department = models.ForeignKey(to='department.Department')
    pto = models.IntegerField(default=20)
    is_deleted = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    roles = models.ManyToManyField(Role, related_name='+')

    def __str__(self):
        return self.username
