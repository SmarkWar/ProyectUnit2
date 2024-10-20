from datetime import datetime

class Proceso:
    id_empleado: str
    id_animal: str
    proceso_que_realizo: str
    fecha_de_proceso: datetime
    observaciones: str

    def __init__(self, id_empleado: str, id_animal: str, proceso_que_realizo: str, fecha_de_proceso: datetime, observaciones: str):
        self.id_empleado = id_empleado
        self.id_animal = id_animal
        self.proceso_que_realizo = proceso_que_realizo
        self.fecha_de_proceso = fecha_de_proceso
        self.observaciones = observaciones

    def mostrar_info(self):
        informacion = f"ID de empleado que realizo el proceso: {self.id_empleado} \nID del animal: {self.id_animal} \nProceso que se realizo: {self.proceso_que_realizo} \nFecha de proceso: {self.fecha_de_proceso} \nObservaciones: {self.observaciones} \n------------------------------------------"
        return informacion