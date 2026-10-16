# =====================================================================
# CLASE TEMPORAL - Se borrará cuando la clase Usuario sea creada
# =====================================================================
class Usuario:
    def __init__(self, id_usuario, nombre, email):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.amigos = []


# =====================================================================
# USUARIO VIP
# =====================================================================
class UsuarioVip(Usuario):
    def __init__(self, id_usuario, nombre, email, insignia="⭐ Miembro VIP"):
        # Llama al constructor de la clase base (Usuario)
        super().__init__(id_usuario, nombre, email)
        
        # Atributos exclusivos del servicio VIP
        self.insignia = insignia
        self.beneficios_activos = True
        self.contenido_exclusivo_visto = 0
