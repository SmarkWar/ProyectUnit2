from usuarios.usuario import Usuario
from empleados.empleado import Empleado
from director.director import Director
from visitantes.visitante import Visitante
from animales.animal import Animal
from visitas.visita import Visita
from usuarios.utils.roles import Rol
from procesos.proceso import Proceso
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
    list_visitas: List[Visita] = []
    lista_procesos: List[Proceso] = []
    lista_director: List[Director] = []
    
    #### GENERAR DIRECTOR ####
    def __init__(self):
        director = Director(id="197515IA3Miia54260", nombre="Miguel", apellido="Garcia", fecha_nacimiento=datetime(day=15, month=6, year=1975), curp="MIGAR750615HGUCIA3", contrasenia="ADMIN1*2")
        self.lista_usuarios.append(director)
        self.lista_director.append(director)

    def validar_inicio_sesion(self, id: str, contrasenia: str):
        director = self.buscar_director_por_id(id_director=id)
        if director is None:
            return
        if director.contrasenia != contrasenia:
                    return None
        return director
    
    ### GENERAR ID's ###
    def generar_id(self, usuario: Usuario):
        nombre = usuario.nombre[:2].upper()
        ano = usuario.fecha_nacimiento.year
        dia = datetime.now().day
        aleatorio = randint(0,100000)
        curp = usuario.curp[-3:].upper()
        caracteres_aleatorios = self.obtener_caracteres_aleatorios(2)
        if usuario.rol == Rol.VISITANTE:
            longitud_mas_uno = len(self.lista_visitantes)+1
            id = f"{ano}{dia}{curp}{nombre}{aleatorio}{caracteres_aleatorios}{longitud_mas_uno}"
        elif usuario.rol != Rol.VISITANTE:
            aleatorio2 = randint(101,9999)
            caracteres_aleatorios2 = self.obtener_caracteres_aleatorios(3)
            longitud_mas_uno = len(self.lista_empleados)+1
            id = f"{ano}{dia}{curp}{nombre}{aleatorio}{caracteres_aleatorios}{aleatorio2}{caracteres_aleatorios2}{longitud_mas_uno}"
        return id
    
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

    def generar_id_visita(self, visita: Visita):
        guia = visita.guia_acargo.nombre[:2].upper()
        dia = datetime.now().day
        caracteres_aleatorios = self.obtener_caracteres_aleatorios(2)
        aleatorio = randint(0,100000)
        id = f"{guia}{dia}{caracteres_aleatorios}{aleatorio}"
        return id
    
    def obtener_caracteres_aleatorios(self, cantidad):
         return ''.join(random.choice(string.ascii_letters) for _ in range(cantidad))
    
    ####EMPLEADO####
    def registrar_empleado(self, empleado: Empleado):
        self.lista_usuarios.append(empleado)
        self.lista_empleados.append(empleado)
        print("\nSe registro con exito al empleado")

    def validar_empleado(self, id_empleado):
        for usuario in self.lista_usuarios:
            if usuario.id == id_empleado:
                return usuario
        return None

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
    
    def asignar_horario_trabajador(self):
        while True:
            try:
                print("*********** HORARIO ***********")
                print("1. 7am a 11am")
                print("2. 11am a 3pm")
                print("3. 3pm a 7pm")
                print("4. 7pm a 11pm")
                opcion= int(input("Seleccione el rol que va a tener el empleado: "))
                
                if 1 <= opcion <= 4: ###Condicion con intervalo##
                    if opcion == 1:
                        horario = "7am a 11am"
                    elif opcion == 2:
                        horario = "11am a 3pm"
                    elif opcion == 3:
                        horario = "3pm a 7pm"
                    elif opcion == 4:
                        horario = "7pm a 11pm"
                    return horario
                    
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
        print(f"No se encontro ningún empleado con el ID: {id} \n")
            
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
        print(f"No se encontro ningún visitante con el ID: {id} \n")
            
    #### ANIMALES ####
    def registrar_animales(self, animal: Animal):
        self.lista_animales.append(animal)
        print("Animales registrados con exito")
        
    def listar_animales(self):
        print("************* ANIMALES *************")
        for animal in self.lista_animales:
            print(animal.mostrar_info_animales())
    
    def eliminar_animal(self, id: str):
        for animal in self.lista_animales:
            if animal.id_animal == id.strip():  
                self.lista_animales.remove(animal)
                print(f"Animal {animal.tipo_animal}, eliminado exitosamente.\n")
                return
        print(f"No se encontro ningún animal con el ID: {id} \n")

    def asignar_tipo_alimentacion(self):
        while True:
            try:
                print("*********** TIPO DE ALIMENTACION ***********")
                print("1. Vegetariana")
                print("2. Carnivora")
                print("3. Omnivora")
                opcion= int(input("Seleccione el rol que va a tener el empleado: "))
                
                if 1 <= opcion <= 4: ###Condicion con intervalo##
                    if opcion == 1:
                        tipo_alimentacion = "Vegetariana"
                    elif opcion == 2:
                        tipo_alimentacion = "Carnivora"
                    elif opcion == 3:
                        tipo_alimentacion = "Omnivira"
                    return tipo_alimentacion
                    
                else:
                    print("Opcion no válida. Por favor, elige un numero entre 1 y 3")
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número entero")
    
    #### VISITAS ####
    def registrar_visitas(self, visita: Visita):
        self.list_visitas.append(visita)
        print("Visita registrada con exito")

    def listar_visitas(self):
        while True:
            try:
                print("************* VISITA *************")
                print("1. Mostrar todas las visitas")
                print("2. Mostrar visitantes registrados a *Una Visita*")
                print("3. Salir")
                opcion= int(input("Seleccione la opcion que desea: "))
                
                if 1 <= opcion <= 3: ###Condicion con intervalo##
                    if opcion == 1:
                        print("************* VISITAS *************")
                        for visita in self.list_visitas:
                            print(visita.mostrar_info())

                    elif opcion == 2:
                        id_visita = input("Ingresa el ID de la visita: ")
                        visita = self.buscar_visita_por_id(id_visita=id_visita)
                        if visita is None:
                            print("No se encontro ninguna visita con el ID ingresado")
                            return
                    
                        visita.mostrar_visitantes_en_la_visita(id_de_la_visita=id_visita)

                    elif opcion == 3:
                        break
                    
                else:
                    print("Opcion no válida. Por favor, elige un numero entre 1 y 3")
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número entero")
    
    def registrar_visitante_en_visitas(self, id_del_visitante: str, id_de_la_visita: str):
        visitante = self.buscar_visitante_por_id(id_visitante=id_del_visitante)
        if visitante is None:
            print("No se encontro ningun visitante con el ID ingresado")
            return
        visita = self.buscar_visita_por_id(id_visita=id_de_la_visita)
        if visita is None:
            print("No se encontro ningun visitante con el ID ingresado")
            return
        visita.registrar_visitante_en_visita(visitante=visitante)
        print("El visitante se registro a la visita con exito")
            
    def incrementar_cantidad(self, cantidad): ###incrementa la cantidad de niños o adultos##
            return cantidad + 1
    
    def incrementa_costo(self, costo_visita, numero_visitas, boleto, visitante: Visitante): ###Incrementa el costo de visita###
        if numero_visitas == 5:
            visitante.numero_visitas = 0
            return costo_visita + 0.8*boleto
        else:
            return costo_visita + boleto
        
        ###PROCESOS###
    
    def registrar_proceso(self, proceso: Proceso):
        self.lista_procesos.append(proceso)
        print("Se registro con exito el proceso")

    def listar_procesos(self):
        print("***** PROCESOS *****")
        for proceso in self.lista_procesos:
            print(proceso.mostrar_info())
    
    def tipo_proceso(self):
        while True:
            try:
                print("**** TIPO DE PROCESO ****")
                print("1. Mantenimiento")
                print("2. Limpieza")
                print("3. Alimentacion")
                print("4. Otro")
                opcion= int(input("Seleccione el rol que va a tener el empleado: "))
                
                if 1 <= opcion <= 4: ###Condicion con intervalo##
                    if opcion == 1:
                        tipo_proceso = "Mantenimiento"
                    elif opcion == 2:
                        tipo_proceso = "Limpieza"
                    elif opcion == 3:
                        tipo_proceso = "Alimentacion"
                    elif opcion == 4:
                        tipo_proceso= input("Ingresa el tipo de proceso: ")
                    return tipo_proceso
                else:
                    print("Opcion no válida. Por favor, elige un numero entre 1 y 4")
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número entero")

    ### Validaciones/ ###

    def buscar_visitante_por_id(self, id_visitante: str):
        for visitante in self.lista_visitantes:
            if visitante.id == id_visitante:
                return visitante
        return None

    def buscar_empleado_por_id(self, id_empleado: str):
        for empleado in self.lista_empleados:
            if empleado.id == id_empleado:
                return empleado
        return None

    def buscar_visita_por_id(self, id_visita: str):
        for visita in self.list_visitas:
            if visita.id_visita == id_visita:
                return visita
        return None    
    
    def buscar_director_por_id(self, id_director: str):
        for director in self.lista_director:
            if director.id == id_director:
                return director
        return None