from empleados.empleado import Empleado
from usuarios.utils.roles import Rol
from datetime import datetime

class Administracion(Empleado):

    def __init__(self, nombre: str, apellido: str, fecha_nacimiento: datetime, curp: str, contrasenia: str, fecha_ingreso_como_trabajador: datetime, rfc: str, salario: float, horario: str):
        super().__init__(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, curp=curp, contrasenia=contrasenia, fecha_ingreso_como_trabajador=fecha_ingreso_como_trabajador, rfc=rfc, salario=salario, horario=horario, rol_trabajador=Rol.ADMINISTRACION)
        