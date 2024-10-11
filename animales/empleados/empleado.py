from usuarios.usuario import Usuario
from datetime import datetime
from usuarios.utils.roles import Rol

class Empleado(Usuario):
    fecha_ingreso_como_trabajador: datetime
    rfc: str
    salario: float
    horario: str
    
    def __init__(self, nombre: str, apellido: str, fecha_nacimiento: datetime, curp: str, contrasenia: str, fecha_ingreso_como_trabajador: datetime, rfc: str, salario: float, horario: str, rol: Rol):
        super().__init__(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, curp=curp, contrasenia=contrasenia, rol=rol)
        self.fecha_ingreso_como_trabajador = fecha_ingreso_como_trabajador
        self.rfc = rfc
        self.salario = salario
        self.horario = horario

    def mostrar_informacion(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        informacion = f"Nombre completo: {nombre_completo} \nFecha de Nacimiento: {self.fecha_nacimiento} \nCurp: {self.curp} \nFecha de Ingreso del trabajador: {self.fecha_ingreso_como_trabajador} \nRFC: {self.rfc} \nSalario: {self.salario} \nHorario: {self.horario} \nRol: {self.rol.value} \n------------------------------------------"
        return informacion