from usuarios.usuario import Usuario
from datetime import datetime
from usuarios.utils.roles import Rol

class Director(Usuario):
    
    def __init__(self, nombre: str, apellido: str, fecha_nacimiento: datetime, curp: str, contrasenia: str):
        super().__init__(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, curp=curp, contrasenia=contrasenia, rol=Rol.DIRECTOR)

    def mostrar_informacion(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        informacion = f"Nombre completo: {nombre_completo} \nFecha de Nacimiento: {self.fecha_nacimiento} \nCurp: {self.curp} \nRol: {self.rol.value} \n------------------------------------------"
        return informacion