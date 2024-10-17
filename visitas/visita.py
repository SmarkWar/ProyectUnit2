 
from datetime import datetime
from random import randint
from empleados.empleado import Empleado
from visitantes.visitante import Visitante
from typing import List

class Visita():
    id_visita: str 
    guia_acargo: Empleado
    fecha_visita: datetime 
    costo_visita: float = 0
    cantidad_niños: int = 0 
    cantidad_adultos: int = 0 
    
    def __init__(self, id_visita: str, guia_acargo: Empleado, fecha_visita: datetime, costo_visita: float, cantidad_niños: int, cantidad_adultos: int):
        self.id_visita = id_visita
        self.guia_acargo = guia_acargo
        self.fecha_visita = fecha_visita
        self.costo_visita = costo_visita
        self.cantidad_niños = cantidad_niños
        self.cantidad_adultos = cantidad_adultos
        self.visitantes: List[Visitante] = []
    
    def registrar_visitante_en_visita(self, visitante: Visitante):
        self.visitantes.append(visitante)

    def mostrar_visitantes_en_la_visita(self, id_de_la_visita: str):
        if id_de_la_visita != self.id_visita:
            print(f"No hay visitantes registrados para la visita con ID {id_de_la_visita}.")
        elif not self.visitantes:
            print(f"La visita con ID {self.id_visita} no tiene visitantes registrados.")
        else:
            print("\n************ Lista de Visitantes registrados ************")
            for visitante in self.visitantes:
                print(visitante.mostrar_info_en_visita())

    def mostrar_info(self):
        info = f"\nID de la visita: {self.id_visita} \nGuia a cargo: {self.guia_acargo.nombre} \nCosto de la visita: {self.costo_visita} \nFecha de la Visita: {self.fecha_visita} \nCantidad de Niños: {self.cantidad_niños} \nCantidad de Adultos: {self.cantidad_adultos} \n------------------------------------------"
        return info