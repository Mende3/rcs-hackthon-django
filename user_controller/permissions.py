# permissions.py
from rest_framework import permissions

class CargoBasedPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        required_permission = getattr(view, 'required_permission', None)
        if not required_permission:
            return False

        user_cargo = request.user.cargo
        
        # Define as permissões para cada cargo
        if user_cargo == 'admin':
            # Admin tem todas as permissões definidas no s.py
            admin_permissions = [
                'criar_admin', 'criar_novo_usuario', 'apagar_usuario', 
                'editar_usuario', 'listar_usuario', 'listar_emails_de_clientes',
                'apagar_emails_de_clientes', 'ver_dashboard', 'ver_config',
                'ver_analise', 'ver_historico', 'ver_perfil'
            ]
            return required_permission in admin_permissions
        
        elif user_cargo == 'usuario normal':
            # Usuário normal tem permissões limitadas
            normal_permissions = [
                'listar_emails_de_clientes', 'apagar_emails_de_clientes',
                'ver_dashboard', 'ver_analise', 'ver_historico', 'ver_perfil'
            ]
            return required_permission in normal_permissions
        
        return False