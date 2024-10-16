from usuarios.usuario import Usuario
from datetime import datetime
from usuarios.utils.roles import Rol

class Visitante(Usuario):
    fecha_registro: datetime
    numero_visitas: int
    
    def __init__(self, id: str, nombre: str, apellido: str, fecha_nacimiento: datetime, curp: str, fecha_registro: datetime, numero_visitas: int):
        super().__init__(id=id, nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, curp=curp, rol=Rol.VISITANTE)
        self.fecha_registro = fecha_registro
        self.numero_visitas = numero_visitas
        
    def mostrar_info_visitante(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        informacion = f"ID: {self.id} \nNombre Completo: {nombre_completo} \nFecha de Nacimiento: {self.fecha_nacimiento} \nCurp: {self.curp} \nFecha de Registro: {self.fecha_registro} \nNumero de visitas: {self.numero_visitas} \nRol: {self.rol.value} \n------------------------------------------"
        return informacion 
    
    def mostrar_info_en_visita(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        informacion = f"ID: {self.id} \nNombre Completo: {nombre_completo} \nFecha de Registro: {self.fecha_registro} \nNumero de visitas: {self.numero_visitas} \n------------------------------------------"
        return informacion 
