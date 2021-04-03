from django.db import models
from employee.models import Employee

class Department(models.Model):
    name = models.CharField(max_length=255)
    # users = models.ForeignKey(myUser, on_delete=models.CASCADE, related_name='user_department')
    department_leader = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='department_leader')
    date_created = models.DateField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
