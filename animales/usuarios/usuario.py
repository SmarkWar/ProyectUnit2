from datetime import datetime
from usuarios.utils.roles import Rol

class Usuario:
    nombre: str
    apellido: str
    fecha_nacimiento: datetime
    curp: str
    contrasenia: str
    rol: Rol
    
    def __init__(self, nombre: str, apellido: str, fecha_nacimiento: datetime, curp: str,  contrasenia: str, rol: Rol):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.curp = curp
        self.contrasenia = contrasenia
        self.rol = rol