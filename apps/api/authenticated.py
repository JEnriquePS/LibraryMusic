from rest_framework.permissions import BasePermission


class CustomAuthenticated(BasePermission):
    """
    Allows access only to authenticated users for POST, PUT and DELETE.
    """

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return bool(request.user and request.user.is_authenticated)
