from django.db import models
# from employee.models import Employee

class Department(models.Model):
    name = models.CharField(max_length=255)
    date_created = models.DateField(auto_now=True)
    department_leader = models.ForeignKey('employee.Employee', on_delete=models.CASCADE, related_name='department_leader', blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
