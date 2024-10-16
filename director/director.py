from usuarios.usuario import Usuario
from datetime import datetime
from usuarios.utils.roles import Rol

class Director(Usuario):
    contrasenia: str

    def __init__(self, id: str, nombre: str, apellido: str, fecha_nacimiento: datetime, curp: str, contrasenia: str):
        super().__init__(id=id, nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, curp=curp, rol=Rol.DIRECTOR)
        self.contrasenia = contrasenia

    def mostrar_informacion(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        informacion = f"ID: {self.id} \nNombre completo: {nombre_completo} \nFecha de Nacimiento: {self.fecha_nacimiento} \nCurp: {self.curp} \nRol: {self.rol.value} \n------------------------------------------"
        return informacion