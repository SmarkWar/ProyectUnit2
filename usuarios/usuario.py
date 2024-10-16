from datetime import datetime
from usuarios.utils.roles import Rol

class Usuario:
    id: str
    nombre: str
    apellido: str
    fecha_nacimiento: datetime
    curp: str
    rol: Rol
    
    def __init__(self, id: str, nombre: str, apellido: str, fecha_nacimiento: datetime, curp: str, rol: Rol):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.curp = curp
        self.rol = rol