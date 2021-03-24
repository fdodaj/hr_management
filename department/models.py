from django.db import models

from app.models import User


class Department(models.Model):
    name = models.CharField(max_length=255)
    users = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_department')
    department_leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='department_leader')
    date_created = models.DateField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
