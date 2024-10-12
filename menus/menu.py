from zoologico.zoologico import Zoologico
from usuarios.usuario import Usuario
from director.director import Director
from visitantes.visitante import Visitante
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
            nombre = input("Ingresa tu nombre: ")
            contrasenia_usuario = input("Ingresa tu contraseña: ")
            usuario = self.zoologico.validar_inicio_sesion(nombre=nombre, contrasenia=contrasenia_usuario)
            
            if usuario is None:
                intentos = self.mostrar_intento_sesion_fallido(intentos_usuarios=intentos)
            else: 
                if usuario.rol == Rol.VISITANTE:
                    pass
                elif usuario.rol == Rol.DIRECTOR:
                    self.mostrar_menu_director(usuario)
                else: 
                    pass

        print("Máximos intentos de inicio de sesion alcanzados. Intente mas tarde")

    def mostrar_intento_sesion_fallido(self, intentos_usuarios):
        print("\nUsuario o contraseña incorrectos. Intente de nuevo")
        return intentos_usuarios + 1
    
    def mostrar_menu_director(self, usuario: Director):
        opcion = 0
        while opcion != 6:
            print("\n***** ZOOLOGICO *****")
            print("1. Registrar empleado")
            print("2. Registrar visitante")
            print("3. Registrar animal")
            print("4. Listar empleados")
            print("5. Listar visitantes")
            print("6. Listar animales")
            print("7. Ver mi informacion")
            print("8. Salir")
            opcion = int(input("Ingresa una opción: "))
            
            if opcion == 1:
                print("------------------------------------------------------------")
                print("\nSeleccionaste registrar empleado \n")
                print("------------------------------------------------------------")
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
                horario = input("Ingresa el horario del empleado: ")
                contrasenia = input("Ingresa la contraseña del empleado ")
                rol = self.zoologico.asignar_rol_trabajador()
                
                empleado = Empleado(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, fecha_ingreso_trabajador=fecha_ingreso_trabajador, rfc=rfc, salario=salario, horario=horario, contrasenia=contrasenia, curp=curp, rol=rol)
                print("El rol del empleado es: ", rol.value)
                self.zoologico.registrar_empleado(empleado=empleado)

            elif opcion == 2:
                print("------------------------------------------------------------")
                print("\nSeleccionaste registrar un visitante \n")
                print("------------------------------------------------------------")
                nombre = input("Ingresa el nombre del visitante: ")
                apellido = input("Ingresa el apellido del visitante: ")
                curp = input("Ingresa la curp del visitante: ")
                
                ano = int(input("Ingresa el año de nacimiento del visitante: "))
                mes = int(input("Ingresa el mes de nacimiento del visitante: "))
                dia = int(input("Ingresa el dia de nacimiento del visitante: "))
                fecha_nacimiento = datetime(ano, mes, dia)
                fecha_registro = datetime.now()
                contrasenia = input("Ingresa la contraseña del visitante: ")
                numero_visitas = 0

                visitante = Visitante(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, fecha_registro=fecha_registro, curp=curp, numero_visitas=numero_visitas, contrasenia=contrasenia)
                self.zoologico.registrar_visitantes(visitante=visitante)
                

            elif opcion == 3:
                print("------------------------------------------------------------")
                print("\nSeleccionaste registrar un animal \n")
                print("------------------------------------------------------------")
                tipo_animal = input("Ingresa el tipo de animal: ")
                peso = input("Ingrese el peso del animal en kg: ")
                enfermedades = input("Ingresa si el animal tiene alguna enfermedad: ")
                frecuencia_alimentacion = input("Ingresa la cantidad de veces que el animal come al dia: ")
                
                ano = int(input("Ingresa el año de nacimiento del animal: "))
                mes = int(input("Ingresa el mes de nacimiento del animal: "))
                dia = int(input("Ingresa el dia de nacimiento del animal: "))
                fecha_nacimiento = datetime(ano, mes, dia)
                fecha_llegada_zoo = datetime.now()
                tipo_alimentacion = input("Ingresa el tipo de alimentacion del animal: ")
                vacunas = input("Ingresa las vacunas que ya posee el animal: ")

                animal = Animal (tipo_animal=tipo_animal, peso=peso, fecha_nacimiento=fecha_nacimiento, fecha_llegada_zoo=fecha_llegada_zoo, enfermedades=enfermedades, frecuencia_alimentacion=frecuencia_alimentacion, tipo_alimentacion=tipo_alimentacion, vacunas=vacunas)
                self.zoologico.registrar_animales(animal=animal)
            
            elif opcion == 4:
                print("************* LISTA DE EMPLEADOS *************")
                print("------------------------------------------------------------")
                self.zoologico.listar_empleados()
                
            elif opcion == 5:
                print("************* LISTA DE VISITANTES *************")
                print("------------------------------------------------------------")
                self.zoologico.listar_visitantes()
                
            elif opcion == 6:
                print("************* LISTA DE ANIMALES *************")
                print("------------------------------------------------------------")
                self.zoologico.listar_animales()

            elif opcion == 7:
                print("************* INFORMACION DE USUARIO *************")
                print(usuario.mostrar_informacion())
            
            else:
                print("\nHasta luego")
                break 