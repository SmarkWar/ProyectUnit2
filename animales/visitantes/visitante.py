from usuarios.usuario import Usuario
from datetime import datetime
from usuarios.utils.roles import Rol

class Visitante(Usuario):
    fecha_registro: datetime
    numero_visitas: int
    
    def __init__(self, nombre: str, apellido: str, fecha_nacimiento: datetime, curp: str, contrasenia: str, fecha_registro: datetime, numero_visitas: int):
        super().__init__(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, curp=curp, contrasenia=contrasenia, rol=Rol.VISITANTE)
        self.fecha_registro = fecha_registro
        self.numero_visitas = numero_visitas