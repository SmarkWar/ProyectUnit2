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
        
    def mostrar_info_visitante(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"Nombre Completo: {nombre_completo} \nFecha de Nacimiento: {self.fecha_nacimiento} \nCurp: {self.curp} \nFecha de Registro: {self.fecha_registro} \nNumero de visitas: {self.numero_visitas} \nRol: {self.rol}"
        return info