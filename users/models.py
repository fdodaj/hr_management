from datetime import timezone
import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
import uuid


# from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    HR = 1
    PD = 2
    EMPLOYEE = 3

    ROLE_CHOICES = (
        (HR, 'hr'),
        (PD, 'pd'),
        (EMPLOYEE, 'Employee')
    )
    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=3)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_by = models.EmailField()
    modified_by = models.EmailField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # objects = CustomUserManager()

    def __str__(self):
        return self.email
