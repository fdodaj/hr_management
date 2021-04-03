from django.db import models
from employee.models import Employee


class Permission(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Denied', 'Denied'),
        ('Accepted', 'Accepted')
    )
    user = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='lorem')
    description = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now=True, blank=True, null=True)
    status = models.CharField(max_length=200, choices=STATUS)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.description
