 
from datetime import datetime
from random import randint

class Visita():
    id_visita: str
    guia_acargo: str
    costo_visita: float = 0
    fecha_visita: datetime
    cantidad_niños: int = 0
    cantidad_adultos: int = 0
    
    def __init__(self, guia_acargo: str, fecha_visita: datetime):
        self.guia_acargo = guia_acargo
        self.fecha_visita = fecha_visita
        self.id_visita = self.generar_id(guia_acargo)
        
    def generar_id(self, guia_acargo: str):
        return f"{guia_acargo[:2]}{randint(1, 10000)}{randint(1, 10000)}"
    
    def mostrar_info(self):
        info = f"\nID de la visita: {self.id_visita}, \nGuia a cargo: {self.guia_acargo}, \nCosto de la visita: {self.costo_visita}, \nFecha de la Visita: {self.fecha_visita}, \nCantidad de Niños: {self.cantidad_niños}, \nCantidad de Adultos: {self.cantidad_adultos}"
    