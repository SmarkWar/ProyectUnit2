 
from datetime import datetime
from random import randint
from empleados.empleado import Empleado
from visitantes.visitante import Visitante
from typing import List

class Visita():
    id_visita: str 
    guia_acargo: str 
    fecha_visita: datetime 
    costo_visita: float = 0
    cantidad_niños: int = 0 
    cantidad_adultos: int = 0 
    visitantes: List[Visitante] = []
    
    def __init__(self, id_visita: str, guia_acargo: str, fecha_visita: datetime, costo_visita: float, cantidad_niños: int, cantidad_adultos: int):
        self.id_visita = id_visita
        self.guia_acargo = guia_acargo
        self.fecha_visita = fecha_visita
        self.costo_visita = costo_visita
        self.cantidad_niños = cantidad_niños
        self.cantidad_adultos = cantidad_adultos
    
    def registrar_visitante_en_visita(self, visitante: Visitante):
        self.visitantes.append(visitante)

    def mostrar_visitantes_en_la_visita(self, id):
        if id == self.id_visita:
            print("\n************ Lista de Visitantes registrados ************")
            for visitante in self.visitantes:
                print(visitante.mostrar_info_en_visita())

    def mostrar_info(self):
        info = f"\nID de la visita: {self.id_visita} \nGuia a cargo: {self.guia_acargo} \nCosto de la visita: {self.costo_visita} \nFecha de la Visita: {self.fecha_visita} \nCantidad de Niños: {self.cantidad_niños} \nCantidad de Adultos: {self.cantidad_adultos}"
        return info