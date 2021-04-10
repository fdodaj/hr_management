# from rest_framework.permissions import BasePermission
#
# class IsRolePermission(BasePermission):
#     role__name = None
#     def has_permission(self, request, view):
#         print(self.role__name, 'queryset')
#         # return True
#         # try:
#         return True
#         # roles = request.user.roles
#         # print(request.user.roles.all().values_list('name',flat=True))
#         # return self.role__name in request.user.roles.all().values_list('name',flat=True)
#         # # except Exception as e:
#         # #     print("ERROR")
#         # #     raise e
#     def has_object_permission(self, request, view, obj):
#         # return True
#         print(self.role__name, 'object')
#         try:
#             return self.has_permission(request, view)
#         except Exception as e:
#             print("ERROR")
#
# class IsHR(IsRolePermission):
#     """
#     Allows access only to community owner users.
#     """
#     role__name = 'HR'
#
#
# class IsManager(IsRolePermission):
#     """
#     Allows access only to community owner users.
#     """
#     role__name = 'MANAGER'
#
# class IsUser(IsRolePermission):
#     """
#     Allows access only to community owner users.
#     """
#     role__name = 'USER'