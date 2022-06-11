from rest_framework.permissions import BasePermission


def developers(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="developer").exists()
