from zoologico.zoologico import Zoologico
from usuarios.usuario import Usuario
from visitas.visita import Visita
from director.director import Director
from visitantes.visitante import Visitante
from procesos.proceso import Proceso
from empleados.empleado import Empleado
from usuarios.utils.roles import Rol
from animales.animal import Animal
from datetime import datetime

class Menu:
    zoologico = Zoologico()
    print("************ BIEVENIDO ************")
    def login(self):
        intentos = 0
        while intentos < 5:
            print("Inicia Sesión para continuar")
            id = input("Ingresa tu ID: ")
            contrasenia_usuario = input("Ingresa tu contraseña: ")
            usuario = self.zoologico.validar_inicio_sesion(id=id, contrasenia=contrasenia_usuario)
            
            if usuario is None:
                intentos = self.mostrar_intento_sesion_fallido(intentos_usuarios=intentos)
            else: 
                if usuario.rol == Rol.DIRECTOR:
                    self.mostrar_menu_director(usuario)

        print("Máximos intentos de inicio de sesion alcanzados. Intente mas tarde")

    def mostrar_intento_sesion_fallido(self, intentos_usuarios):
        print("\nUsuario o contraseña incorrectos. Intente de nuevo")
        return intentos_usuarios + 1
    
    def mostrar_menu_director(self, usuario: Director):
        while True:
            try:
                print("\n***** ZOOLOGICO *****")
                print("1. Registrar empleado")
                print("2. Registrar visitante")
                print("3. Registrar animal")
                print("4. Registrar visita guiada")
                print("5. Registrar proceso")
                print("6. Listar empleados")
                print("7. Listar visitantes")
                print("8. Listar animales")
                print("9. Listar Visitas")
                print("10. Listar Procesos")
                print("11. Eliminar empleado")
                print("12. Eliminar visitante")
                print("13. Eliminar un animal")
                print("14. Ver mi informacion")
                print("15. Salir")
                opcion = int(input("Ingresa una opción: "))
                
                if 1<= opcion <= 15:
                    if opcion == 1:
                        print("------------------------------------------------------------ \nSeleccionaste registrar empleado \n------------------------------------------------------------")
                        nombre = input("Ingresa el nombre del empleado: ")
                        apellido = input("Ingresa el apellido del empleado: ")
                        curp = input("Ingresa la curp del empleado: ")
                        ano = int(input("Ingresa el año de nacimiento del empleado: "))
                        mes = int(input("Ingresa el mes de nacimiento del empleado: "))
                        dia = int(input("Ingresa el dia de nacimiento del empleado: "))
                        fecha_nacimiento = datetime(ano, mes, dia)
                        fecha_ingreso_trabajador = datetime.now()
                        rfc = input("Ingresa el RFC del empleado: ")
                        salario = input("Ingresa el sueldo del empleado: ")
                        horario = self.zoologico.asignar_horario_trabajador()
                        rol = self.zoologico.asignar_rol_trabajador()

                        empleado = Empleado("", nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, fecha_ingreso_trabajador=fecha_ingreso_trabajador, rfc=rfc, salario=salario, horario=horario, curp=curp, rol=rol)
                        id = self.zoologico.generar_id(empleado)
                        empleado.id = id
                        print("El ID del empledo es: ", id)
                        self.zoologico.registrar_empleado(empleado=empleado)

                    elif opcion == 2:
                        print("------------------------------------------------------------ \nSeleccionaste registrar un visitante \n------------------------------------------------------------")
                        nombre = input("Ingresa el nombre del visitante: ")
                        apellido = input("Ingresa el apellido del visitante: ")
                        curp = input("Ingresa la curp del visitante: ")
                        ano = int(input("Ingresa el año de nacimiento del visitante: "))
                        mes = int(input("Ingresa el mes de nacimiento del visitante: "))
                        dia = int(input("Ingresa el dia de nacimiento del visitante: "))
                        fecha_nacimiento = datetime(ano, mes, dia)
                        fecha_registro = datetime.now()
                        numero_visitas = 0

                        visitante = Visitante("", nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, fecha_registro=fecha_registro, curp=curp, numero_visitas=numero_visitas)
                        id = self.zoologico.generar_id(visitante)
                        visitante.id = id
                        print("El ID del visitante es: ", id)
                        self.zoologico.registrar_visitantes(visitante=visitante)
                        
                    elif opcion == 3:
                        print("------------------------------------------------------------ \nSeleccionaste registrar un animal \n------------------------------------------------------------")
                        tipo_animal = input("Ingresa el tipo de animal: ")
                        peso = input("Ingrese el peso del animal en kg: ")
                        enfermedades = input("Ingresa si el animal tiene alguna enfermedad: ")
                        frecuencia_alimentacion = input("Ingresa la cantidad de veces que el animal come al dia: ")
                        ano = int(input("Ingresa el año de nacimiento del animal: "))
                        mes = int(input("Ingresa el mes de nacimiento del animal: "))
                        dia = int(input("Ingresa el dia de nacimiento del animal: "))
                        fecha_nacimiento = datetime(ano, mes, dia)
                        fecha_llegada_zoo = datetime.now()
                        tipo_alimentacion = self.zoologico.asignar_tipo_alimentacion()
                        vacunas = input("Ingresa las vacunas que ya posee el animal: ")

                        animal = Animal("", tipo_animal=tipo_animal, peso=peso, fecha_nacimiento=fecha_nacimiento, fecha_llegada_zoo=fecha_llegada_zoo, enfermedades=enfermedades, frecuencia_alimentacion=frecuencia_alimentacion, tipo_alimentacion=tipo_alimentacion, vacunas=vacunas)
                        id_animal = self.zoologico.generar_id_animal(animal=animal)
                        animal.id_animal = id_animal
                        print("El ID del animal es: ", id_animal)
                        self.zoologico.registrar_animales(animal=animal)
                    
                    elif opcion == 4:
                        print("------------------------------------------------------------ \nSeleccionaste registrar una visita \n------------------------------------------------------------")
                        
                        guia_acargo = input("Ingresa el ID del guia a cargo de la visita: ")
                        for empleado in self.zoologico.lista_empleados:
                            if empleado.id == guia_acargo:
                                fecha_visita = datetime.now().day
                                visita = Visita("", guia_acargo=guia_acargo, fecha_visita=fecha_visita, costo_visita=0, cantidad_adultos=0, cantidad_niños=0)
                                id_visita = self.zoologico.generar_id_visita(visita=visita)
                                visita.id_visita = id_visita
                                print("El ID de la visita es: ", visita.id_visita)
                                while True:
                                    try:
                                        print("\n*********** VISITA ***********")
                                        print("1. Registrar visitante")
                                        print("2. Mostrar visitantes registrados a la visita")
                                        print("3. Salir")
                                        opcion= int(input("Seleccione la opcion que desea: "))
                                        if 1 <= opcion <= 3: ###Condicion con intervalo##
                                            if opcion == 1:
                                                id_visitante = input("Ingresa el ID del visitante: ")
                                                for visitante in self.zoologico.lista_visitantes:
                                                    if visitante.id == id_visitante:
                                                        self.zoologico.registrar_visitante_en_visitas(visitante=visitante, visita=visita)
                                                        ano_nacimiento = visitante.fecha_nacimiento.year
                                                        fechaparacalcularedad = (datetime.now().year - 18)
                                                        cantidad_niños = visita.cantidad_niños
                                                        cantidad_adultos = visita.cantidad_adultos
                                                        costo_de_visita = visita.costo_visita
                                                        numero_visitas = visitante.numero_visitas + 1
                                                        visitante.numero_visitas = numero_visitas

                                                        if ano_nacimiento <= fechaparacalcularedad:
                                                            cantidad_adultos = self.zoologico.incrementar_cantidad(cantidad=cantidad_adultos)
                                                            visita.cantidad_adultos = cantidad_adultos
                                                            costo_boleto = 100
                                                        else:
                                                            cantidad_niños = self.zoologico.incrementar_cantidad(cantidad=cantidad_niños)
                                                            visita.cantidad_niños = cantidad_niños
                                                            costo_boleto = 50
                                                            
                                                        costo = self.zoologico.incrementa_costo(costo_visita=costo_de_visita, numero_visitas=numero_visitas, boleto=costo_boleto, visitante=visitante)
                                                        visita.costo_visita = costo
                                                            
                                            elif opcion == 2:
                                                visita.mostrar_visitantes_en_la_visita(id=id_visita)

                                            elif opcion == 3:
                                                break
                                                
                                        else:
                                            print("Opcion no válida. Por favor, elige un numero entre 1 y 3")
                                    except ValueError:
                                        print("Entrada no válida. Por favor, ingresa un número entero")
                                self.zoologico.registrar_visitas(visita=visita)
                     
                    elif opcion == 5:
                        print("------------------------------------------------------------ \nSeleccionaste registrar un proceso \n------------------------------------------------------------")
                        while True:
                            id_empleado = input("Ingrese el ID del empleado que realizo el proceso: ")
                            usuario = self.zoologico.validar_empleado(id_empleado=id_empleado)
                            
                            if usuario is None:
                                print("No existe ningun empleado con ese ID")
                            else: 
                                if usuario.rol == Rol.MANTENIMIENTO:
                                    id_de_animal = input("Ingrese el ID del animal: ")
                                    proceso_que_realizo = datetime.now()
                                    fecha_de_proceso =
                                    observaciones =

                    elif opcion == 6:
                        self.zoologico.listar_empleados()
                        
                    elif opcion == 7:
                        self.zoologico.listar_visitantes()
                        
                    elif opcion == 8:
                        self.zoologico.listar_animales()

                    elif opcion == 9:
                        self.zoologico.listar_visitas()

                    elif opcion == 10:
                        pass

                    elif opcion == 11:
                        print("************* ELIMINAR UN EMPLEADO *************")
                        id = input("\nIngresa el id del empleado: ")
                        self.zoologico.eliminar_empleado(id=id)
                    
                    elif opcion == 12:
                        print("************* ELIMINAR UN ASISTENTE *************")
                        id = input("\nIngresa el id del visitante: ")
                        self.zoologico.eliminar_visitante(id=id)
                    
                    elif opcion == 13:
                        print("************* ELIMINAR UN ANIMAL *************")
                        id = input("\nIngresa el id del animal: ")
                        self.zoologico.eliminar_animal(id=id)
                    
                    elif opcion == 14:
                        print("************* INFORMACION DE USUARIO *************")
                        print(usuario.mostrar_informacion())


                    else:
                        print("\nHasta luego")
                        break 

                else:
                    print("Opcion no válida. Por favor, elige un numero entre 1 y 11")
                     
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número entero")
