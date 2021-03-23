from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class Role(models.Model):
    ROLES = (
        ('HR', 'HR'),
        ('Department_manager', 'Department_manager'),
        ('User', 'User')
    )
    role = models.CharField(max_length=255, choices=ROLES)
    date_created = models.DateField(auto_now=True)
    date_deleted = models.DateField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.role


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now=True)
    hire_date = models.DateTimeField(auto_now=True)
    paid_time_off = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='user_roles')

    def __str__(self):
        return self.first_name + self.last_name


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
    date_deleted = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.description


class Holiday(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    from_date = models.DateField()
    to_date = models.DateField()
    date_created = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=255)
    users = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_department')
    department_leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='department_leader')
    date_created = models.DateField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
