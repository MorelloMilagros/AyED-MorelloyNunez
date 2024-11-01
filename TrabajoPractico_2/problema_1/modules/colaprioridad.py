import heapq
from datetime import datetime

class Triaje:
    def __init__(self):
        # Usaremos un heap para gestionar la prioridad de los pacientes
        self.cola_prioridad = []
        self.pacientes_dict = {}
        self.contador_id = 0  # Contador único para asegurar orden de llegada en pacientes con la misma prioridad

    def agregar_paciente(self, nombre, prioridad):
        # Creamos un ID único usando la fecha y el contador
        self.contador_id += 1
        paciente = (prioridad, self.contador_id, nombre)  # Almacenamos prioridad, ID único y nombre
        heapq.heappush(self.cola_prioridad, paciente)  # Insertamos en la cola de prioridad
        self.pacientes_dict[nombre] = paciente  # Guardamos en el diccionario para acceso rápido

    def atender_paciente(self):
        if self.cola_prioridad:
            # Extraemos el paciente de mayor prioridad (menor valor de prioridad numérica)
            prioridad, _, nombre = heapq.heappop(self.cola_prioridad)
            # Eliminamos el paciente del diccionario
            del self.pacientes_dict[nombre]
            # Generamos el mensaje de atención
            mensaje_atencion = (
                f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n"
                f"****************************************\n"
                f"Se atiende el paciente: {nombre:<15} -> {prioridad}\n"
                f"****************************************\n"
            )
            return mensaje_atencion
        else:
            return "No hay pacientes en espera."

    def mostrar_pacientes_en_espera(self):
        if not self.cola_prioridad:
            return "No hay pacientes en espera."

        pacientes = [
            f"{nombre:<15} -> {prioridad}"
            for prioridad, _, nombre in sorted(self.cola_prioridad)
        ]
        pacientes_espera = "\n".join(pacientes)
        mensaje_espera = (
            f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n"
            f"Pacientes que faltan atenderse: {len(self.cola_prioridad)}\n"
            f"{pacientes_espera}\n"
            f"{'-*-' * 10}"
        )
        return mensaje_espera
