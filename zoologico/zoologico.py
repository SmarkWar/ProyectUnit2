from usuarios.usuario import Usuario
from empleados.empleado import Empleado
from director.director import Director
from visitantes.visitante import Visitante
from animales.animal import Animal
from usuarios.utils.roles import Rol
from typing import List
from datetime import datetime
from random import randint
import random
import string

class Zoologico:
    lista_usuarios: List[Usuario] = []
    lista_empleados: List[Empleado] = []
    lista_visitantes: List[Visitante] = []
    lista_animales: List[Animal] = []
    
    #### GENERAR DIRECTOR ####
    def __init__(self):
        director = Director(id="197515IA3Miia54260", nombre="Miguel", apellido="Garcia", fecha_nacimiento=datetime(day=15, month=6, year=1975), curp="MIGAR750615HGUCIA3", contrasenia="ADMIN1*2")
        self.lista_usuarios.append(director)

    def validar_inicio_sesion(self, id: str, contrasenia: str):
        for usuario in self.lista_usuarios:
            if usuario.id == id:
                if usuario.contrasenia == contrasenia:
                    return usuario
        return None
    
    ### GENERAR ID ###
    def generar_id(self, usuario: Usuario):
        nombre = usuario.nombre[:2].upper()
        ano = usuario.fecha_nacimiento.year
        dia = datetime.now().day
        aleatorio = randint(0,100000)
        curp = usuario.curp[-3:].upper()
        if usuario.rol == Rol.VISITANTE:
            caracteres_aleatorios = self.obtener_caracteres_aleatorios(2)
            longitud_mas_uno = len(self.lista_visitantes)+1
            id = f"{ano}{dia}{curp}{nombre}{aleatorio}{caracteres_aleatorios}{longitud_mas_uno}"
        elif usuario.rol != Rol.VISITANTE:
            aleatorio2 = randint(101,9999)
            caracteres_aleatorios = self.obtener_caracteres_aleatorios(2)
            caracteres_aleatorios2 = self.obtener_caracteres_aleatorios(3)
            longitud_mas_uno = len(self.lista_empleados)+1
            id = f"{ano}{dia}{curp}{nombre}{aleatorio}{caracteres_aleatorios}{aleatorio2}{caracteres_aleatorios2}{longitud_mas_uno}"
        return id
    
    def obtener_caracteres_aleatorios(self, cantidad):
         return ''.join(random.choice(string.ascii_letters) for _ in range(cantidad))
    
    ####EMPLEADO####
    def registrar_empleado(self, empleado: Empleado):
        self.lista_usuarios.append(empleado)
        self.lista_empleados.append(empleado)
        print("\nSe registro con exito al empleado\n")

    def listar_empleados(self):
        print("************* EMPLEADOS *************")
        for empleado in self.lista_empleados:
            print(empleado.mostrar_informacion())

    def asignar_rol_trabajador(self):
        while True:
            try:
                print("*********** ROLES ***********")
                print("1. Rol de administracion")
                print("2. Rol de Veterinario")
                print("3. Rol de guia")
                print("4. Rol de Mantenimiento")
                opcion= int(input("Seleccione el rol que va a tener el empleado: "))
                
                if 1 <= opcion <= 4: ###Condicion con intervalo##
                    if opcion == 1:
                        rol=Rol.ADMINISTRACION
                    elif opcion == 2:
                        rol=Rol.VETERINARIO
                    elif opcion == 3:
                        rol=Rol.GUIA
                    elif opcion == 4:
                        rol=Rol.MANTENIMIENTO
                    return rol
                    
                else:
                    print("Opcion no válida. Por favor, elige un numero entre 1 y 4")
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número entero")

    def eliminar_empleado(self, id: str):
        for empleado in self.lista_empleados:
            if empleado.id == id.strip(): #CAMBIEEEEEEEEEE
                self.lista_empleados.remove(empleado)
                print(f"Empleado {empleado.nombre} {empleado.apellido}, eliminado exitosamente.\n")
                return 
            
    #### VISITANTES ####
    def registrar_visitantes(self, visitante: Visitante):
        self.lista_usuarios.append(visitante)
        self.lista_visitantes.append(visitante)
        print("Visitantes registrados con exito")
        
    def listar_visitantes(self):
        print("************* VISITANTES *************")
        for visitante in self.lista_visitantes:
            print(visitante.mostrar_info_visitante())

    def eliminar_visitante(self, id: str):
        for visitante in self.lista_visitantes:
            if visitante.id == id.strip(): #CAMBIEEEEEEEEEE
                self.lista_visitantes.remove(visitante)
                print(f"Visitante {visitante.nombre} {visitante.apellido}, eliminado exitosamente.\n")
                return
            
    #### ANIMALES ####
    def registrar_animales(self, animal: Animal):
        self.lista_animales.append(animal)
        print("Animales registrados con exito")
        
    def listar_animales(self):
        print("************* ANIMALES *************")
        for animal in self.lista_animales:
            print(animal.mostrar_info_animales())

    def generar_id_animal(self, animal: Animal):
        alimentacion = animal.tipo_alimentacion[:3].upper()
        ano = animal.fecha_nacimiento.year
        dia = animal.fecha_llegada__zoo.day
        tipo = animal.tipo_animal[:3].upper()
        aleatorio = randint(0,100000)
        aleatorio2 = randint(101,9999)
        caracteres_aleatorios = self.obtener_caracteres_aleatorios(2)
        caracteres_aleatorios2 = self.obtener_caracteres_aleatorios(3)
        longitud_mas_uno = len(self.lista_animales)+1
        id = f"{alimentacion}{ano}{dia}{tipo}{aleatorio}{caracteres_aleatorios}{aleatorio2}{caracteres_aleatorios2}{longitud_mas_uno}"
        return id
    
    def eliminar_animal(self, id: str):
        for animal in self.lista_animales:
            if animal.id_animal == id.strip():  
                self.lista_animales.remove(animal)
                print(f"Animal {animal.tipo_animal}, eliminado exitosamente.\n")
                return
    
