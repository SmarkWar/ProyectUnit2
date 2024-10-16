from usuarios.usuario import Usuario
from datetime import datetime
from usuarios.utils.roles import Rol

class Empleado(Usuario):
    fecha_ingreso_trabajador: datetime
    rfc: str
    salario: float
    horario: str
    
    def __init__(self, id: str, nombre: str, apellido: str, fecha_nacimiento: datetime, curp: str, fecha_ingreso_trabajador: datetime, rfc: str, salario: float, horario: str, rol: Rol):
        super().__init__(id=id, nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, curp=curp, rol=rol)
        self.fecha_ingreso_trabajador = fecha_ingreso_trabajador
        self.rfc = rfc
        self.salario = salario
        self.horario = horario

    def mostrar_informacion(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        informacion = f"ID: {self.id} \nNombre completo: {nombre_completo} \nFecha de Nacimiento: {self.fecha_nacimiento} \nCurp: {self.curp} \nFecha de Ingreso del trabajador: {self.fecha_ingreso_trabajador} \nRFC: {self.rfc} \nSalario: {self.salario} \nHorario: {self.horario} \nRol: {self.rol.value} \n------------------------------------------"
        return informacion