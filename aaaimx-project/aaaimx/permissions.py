from rest_framework.permissions import BasePermission

class UserPermission(BasePermission):
    """
    A base class from which all permission classes should inherit.
    """
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        user = request.user
        user_id = view.kwargs.get('pk')

        if request.method == 'POST':
            return user.groups.filter(name__in=['Leader'])

        if request.method == 'GET' and not user_id:
            return user.groups.filter(name__in=['Leader', 'Guest'])

        return True

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if `has_permission` is `True` and object permission is granted, `False` otherwise.
        """
        return True
