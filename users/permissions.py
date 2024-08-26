from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission


class IsActive(BasePermission):
    """
    Проверяет, является ли пользователь аутентифицированным и активным.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            raise PermissionDenied('Вы не аутентифицированы!')
        if not request.user.is_active:
            raise PermissionDenied('Вы не активны!')
        return True


class IsOwner(BasePermission):
    """
    Проверяет, является ли текущий пользователь владельцем объекта, с которым он пытается взаимодействовать.
    """
    message = 'Вы не являетесь владельцем!'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False
