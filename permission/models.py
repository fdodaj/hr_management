from django.db import models
from app.models import User


class Permission(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Denied', 'Denied'),
        ('Accepted', 'Accepted')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_permissions')
    description = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now=True, blank=True, null=True)
    status = models.CharField(max_length=200, choices=STATUS)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.description
