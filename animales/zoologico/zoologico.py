from usuarios.usuario import Usuario
from empleados.empleado import Empleado
from director.director import Director
from empleados.administracion import administracion
from empleados.guias import guia
from empleados.mantenimiento import mantenimiento
from empleados.veterinarios import veterinario
from visitantes.visitante import Visitante
from usuarios.utils.roles import Rol
from typing import List
from datetime import datetime
from random import randint

class Zoologico:
    lista_usuarios: List[Usuario] = []
    lista_empleados: List[Empleado] = []
    lista_visitantes: List[Visitante] = []
    
    def __init__(self): ###GENERAR DIRECTOR###
        director = Director(nombre="Miguel", apellido="Garcia", fecha_nacimiento=datetime(day=15, month=6, year=1975), curp="MIGAR750615HGUCIA3", contrasenia="ADMIN1*2")
        self.lista_usuarios.append(director)

    def validar_inicio_sesion(self, nombre: str, contrasenia: str):
        for usuario in self.lista_usuarios:
            if usuario.nombre == nombre:
                if usuario.contrasenia == contrasenia:
                    return usuario
        return None
    
    ####EMPLEADO####
    def registrar_empleado(self, empleado: Empleado):
        self.lista_usuarios.append(empleado)
        self.lista_empleados.append(empleado)
        print("\nSe registro con exito al empleado\n")

    def listar_empleados(self):
        print("************* Empleados *************")
        for empleado in self.lista_empleados:
            print(empleado.mostrar_informacion())

    def asignar_rol_trabajador(self):
        print("*********** ROLES ***********")
        print("1. Rol de administracion")
        print("2. Rol de Veterinario")
        print("3. Rol de guia")
        print("4. Rol de Mantenimiento")
        opcion= int(input("Seleccione el rol que va a tener el empleado: "))

        while True:
            if opcion == 1:
                rol=Rol.ADMINISTRACION
                return rol
            elif opcion == 2:
                rol=Rol.VETERINARIO
                return rol
            elif opcion == 3:
                rol=Rol.GUIA
                return rol
            elif opcion == 4:
                rol=Rol.MANTENIMIENTO
                return rol
        