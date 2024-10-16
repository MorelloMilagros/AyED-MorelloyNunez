# monticulo_pacientes.py

from modules.monticulo import MonticuloBinario
from modules.paciente import Paciente

class TriajePacientes:
    def __init__(self):
        # Crea un montículo para almacenar los pacientes en función de su nivel de riesgo
        self.monticulo = MonticuloBinario()

    def agregar_paciente(self, paciente):
        # Inserta el paciente en el montículo usando el nivel de riesgo como clave
        # Para priorizar, insertamos una tupla (riesgo, paciente)
        self.monticulo.insertar((paciente.get_riesgo(), paciente))

    def atender_paciente(self):
        # Elimina y retorna el paciente con mayor prioridad de riesgo
        if self.monticulo.tamanoActual > 0:
            _, paciente = self.monticulo.eliminarMin()
            return paciente
        return None

    def pacientes_en_espera(self):
        # Devuelve la lista de pacientes restantes en espera (para visualizar)
        return [paciente for _, paciente in self.monticulo.listaMonticulo[1:]]
