from rolepermissions.roles import AbstractUserRole

class Administrador (AbstractUserRole) :
    available_permissions = {
        'criar_admin': True,
        'criar_novo_usuario': True,
        'apagar_usuario': True,
        'editar_usuario': True,
        'listar_usuario': True,
        'listar_emails_de_clientes': True,
        'apagar_emails_de_clientes': True,
        'ver_dashboard': True,
        'ver_config': True,
        'ver_analise': True,
        'ver_historico': True,
        'ver_perfil': True,
    }

class UsuarioNormal (AbstractUserRole) :
     available_permissions = {
        'listar_emails_de_clientes': True,
        'apagar_emails_de_clientes': True,
        'ver_dashboard': True,
        'ver_analise': True,
        'ver_historico': True,
        'ver_perfil': True,
    }

