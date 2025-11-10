from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        role = request.auth.get("rol") if request.auth else None  
        return role == "ADMINISTRADOR"


class IsOperario(BasePermission):
    def has_permission(self, request, view):
        role = request.auth.get("rol") if request.auth else None  
        return role == "OPERARIO"


class IsPlanner(BasePermission):
    def has_permission(self, request, view):
        role = request.auth.get("rol") if request.auth else None  
        return role == "PLANIFICADOR"


class IsAtencion(BasePermission):
    def has_permission(self, request, view):
        role = request.auth.get("rol") if request.auth else None  
        return role == "ATENCION"
    
def ORPermission(*permissions):
    """
    Devuelve una clase de permiso que hace OR lógico entre las que recibe.
    """
    class _ORPermission(BasePermission):
        def has_permission(self, request, view):
            return any(p().has_permission(request, view) for p in permissions)
    return _ORPermission