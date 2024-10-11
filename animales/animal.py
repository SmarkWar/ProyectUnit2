from usuarios.usuario import Usuario
from datetime import datetime
from usuarios.utils.roles import Rol

class Animal(Usuario):
    
    tipo_animal: str
    fecha_llegada__zoo: datetime
    peso: float
    enfermedades: str
    frecuencia_alimentacion: int
    tipo_alimentacion: str
    vacunas: bool
    
    def __init__(self, tipo_animal: str,
                 fecha_nacimiento: str,
                 fecha_llegada_zoo: datetime,
                 peso: float,
                 enfermedades: str,
                 frecuencia_alimentacion: str,
                 tipo_alimentacion: str,
                 vacunas: bool,
                 rol: Rol):
        
        super().__init__(fecha_nacimiento = fecha_nacimiento, rol = rol)
        
        self.tipo_animal = tipo_animal
        self.fecha_llegada__zoo = fecha_llegada_zoo
        self.peso = peso
        self.enfermedades = enfermedades
        self.frecuencia_alimentacion = frecuencia_alimentacion
        self.tipo_alimentacion = tipo_alimentacion
        self.vacunas = vacunas
        
    def mostrar_informacion(self):
        informacion = f"Tipo de Animal: {self.tipo_animal},
        \nFecha de Nacimiento: {self.fecha_nacimiento},
        \nFecha de llegada al zoologico: {self.fecha_llegada__zoo},
        \nPeso: {self.peso},
        \nEnfermedades: {self.enfermedades},
        \nFrecuencia de Alimentacion: {self.frecuencia_alimentacion},
        \nTipo de Alimentacion: {self.tipo_alimentacion},
        \nVacunas: {self.vacunas}"
        return informacion