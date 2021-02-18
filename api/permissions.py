from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if view.action == 'create':
            return True
        user = view.get_object()
        return request.user.id == user.id