from django.db import models
from employee.models import Employee
from datetime import date
from holiday.models import Holiday


class Request(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Denied', 'Denied'),
        ('Accepted', 'Accepted')
    )
    user = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='lorem')
    date = models.DateField()
    description = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=STATUS, default=STATUS[0][0])
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.description


