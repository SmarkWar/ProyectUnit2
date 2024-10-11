from datetime import datetime
from usuarios.utils.roles import Rol

class Usuario:
    nombre: str
    apellido: str
    rol: Rol
    contrasenia: str
    curp: str
    fecha_nacimiento: datetime
    
    def __init__(self, nombre: str, apellido: str, rol: Rol,  contrasenia: str, curp: str, fecha_nacimiento: datetime):
        self.nombre = nombre
        self.apellido = apellido
        self.rol = rol
        self.contrasenia = contrasenia
        self.curp = curp
        self.fecha_nacimiento = fecha_nacimiento
 
 