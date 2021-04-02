from django.db import models
from django.contrib.auth.models import User,AbstractUser

class Employee(AbstractUser):
    department = models.CharField(max_length=100, null=True, blank=True)
    pto = models.IntegerField(null=True, blank=True)

    exclude = ('groups','user_permissions')

    def __str__(self):
        return self.username


# class Role(models.Model):
#     ROLES = (
#         ('HR', 'HR'),
#         ('Department_manager', 'Department_manager'),
#         ('User', 'User')
#     )
#     role = models.CharField(max_length=255, choices=ROLES, default='User')
#     date_created = models.DateField(auto_now=True)
#     date_deleted = models.DateField(blank=True, null=True)
#     is_deleted = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.role

# class myUser(AbstractBaseUser):
#     name = models.CharField(max_length=255, default='')
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # email = models.CharField(max_length=50)


    # is_active = models.BooleanField(_('active'), default=True)
    # avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
#
# class User(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
#     username = models.CharField(max_length=255, default='')
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     date_created = models.DateTimeField(auto_now=True)
#     hire_date = models.DateTimeField(auto_now=True)
#     paid_time_off = models.CharField(max_length=100)
#     is_deleted = models.BooleanField(default=False)
#     role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='user_roles')
#
#     def __str__(self):
#         return self.first_name + self.last_name
#
#     def __str__(self):
#         return self.role
#
#     def delete(self, using=None, keep_parents=False):
#         pass

# class Role(models.Model):
#     role_name = models.CharField()
#
# class UserRole(models.Model):
#     role = models.ForeignKey(Role)
#     user = models.ForeignKey(User)
#
#     start
#     end
#     active
#
# u1 = User(id=10)
# u1.user_role