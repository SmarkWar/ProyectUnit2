from zoologico.zoologico import Zoologico
from usuarios.usuario import Usuario
from director.director import Director
from visitantes.visitante import Visitante
from empleados.empleado import Empleado
from usuarios.utils.roles import Rol
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
            print("5. Ver mi informacion")
            print("6. Salir")
            opcion = int(input("Ingresa una opción: "))
            
            if opcion == 1:
                print("\nSeleccionaste registrar empleado \n")
                nombre = input("Ingresa el nombre del empleado: ")
                apellido = input("Ingresa el apellido del empleado: ")
                curp = input("Ingresa la curp del empleado: ")
                
                ano = int(input("Ingresa el año de nacimiento del empleado: "))
                mes = int(input("Ingresa el mes de nacimiento del empleado: "))
                dia = int(input("Ingresa el dia de nacimiento del empleado: "))
                fecha_nacimiento = datetime(ano, mes, dia)
                fecha_ingreso_como_trabajador = datetime.now()
                rfc = input("Ingresa el RFC del empleado: ")
                salario = input("Ingresa el sueldo del empleado: ")
                horario = input("Ingresa el horario del empleado: ")
                contrasenia = input("Ingresa la contraseña del empleado ")
                rol = self.zoologico.asignar_rol_trabajador()
                
                empleado = Empleado(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, fecha_ingreso_como_trabajador=fecha_ingreso_como_trabajador, rfc=rfc, salario=salario, horario=horario, contrasenia=contrasenia, curp=curp, rol=rol)
                print("El rol del empleado es: ", rol.value)
                self.zoologico.registrar_empleado(empleado=empleado)

            elif opcion == 2:
                print("\nSeleccionaste registrar empleado \n")
                pass

            elif opcion == 3:
                print("\nSeleccionaste registrar empleado \n")
                pass
            
            elif opcion == 4:
                self.zoologico.listar_empleados()

            elif opcion == 5:
                print("************* INFORMACION DE USUARIO *************")
                print(usuario.mostrar_informacion())
            
            else:
                print("\nHasta luego")
                break 