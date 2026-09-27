from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    # GET/HEAD/OPTIONS доступны всем.
    # Изменение и удаление — только авторизованным.
    #
    # В модели Product нет поля user, поэтому проверка владельца
    # через obj.user здесь невозможна.
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated)


class IsAdminOrReadOnly(permissions.BasePermission):
    # GET доступен всем, POST/PUT/PATCH/DELETE — только администратору.
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
