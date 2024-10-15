from datetime import datetime

class Animal():
    id_animal: str
    tipo_animal: str
    fecha_llegada__zoo: datetime
    fecha_nacimiento: datetime
    peso: float
    enfermedades: str
    frecuencia_alimentacion: int
    tipo_alimentacion: str
    vacunas: bool
    
    def __init__(self, id_animal: str, tipo_animal: str, fecha_nacimiento: datetime, fecha_llegada_zoo: datetime, peso: float, enfermedades: str, frecuencia_alimentacion: str, tipo_alimentacion: str, vacunas: bool):
        self.id_animal = id_animal
        self.tipo_animal = tipo_animal
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_llegada__zoo = fecha_llegada_zoo
        self.peso = peso
        self.enfermedades = enfermedades
        self.frecuencia_alimentacion = frecuencia_alimentacion
        self.tipo_alimentacion = tipo_alimentacion
        self.vacunas = vacunas
        
    def mostrar_info_animales(self):
        informacion = f"ID: {self.id_animal} \nTipo de Animal: {self.tipo_animal} \nFecha de Nacimiento: {self.fecha_nacimiento} \nFecha de llegada al zoologico: {self.fecha_llegada__zoo} \nPeso: {self.peso}kg \nEnfermedades: {self.enfermedades} \nFrecuencia de Alimentacion: {self.frecuencia_alimentacion} veces al dia \nTipo de Alimentacion: {self.tipo_alimentacion} \nVacunas: {self.vacunas}"
        return informacion