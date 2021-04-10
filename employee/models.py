from django.db import models
from django.contrib.auth.models import User, AbstractUser
# from role.models import
from role.models import Role
from department.models import Department

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Employee(AbstractUser):
    department = models.ForeignKey(Department, on_delete=models.CASCADE,blank=True, null=True)
    # employee_department = models.ForeignKey(to='department.Department')
    pto = models.IntegerField(default=20)
    is_deleted = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    roles = models.ManyToManyField(Role, related_name='+')

    def __str__(self):
        return self.username



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)