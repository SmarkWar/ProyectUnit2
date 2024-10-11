from usuarios.usuario import Usuario
from datetime import datetime
from usuarios.utils.roles import Rol

class Visitante(Usuario):
    fecha_registro: datetime
    numero_visitas: int
    
    def __init__(self, nombre: str, apellido: str, contrasenia: str, fecha_nacimiento: datetime, curp: str, numero_visitas: int):
        super().__init__(nombre=nombre, apellido=apellido, contrasenia=contrasenia, rol=Rol.VISITANTE, curp=curp)
 