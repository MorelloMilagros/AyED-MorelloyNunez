# monticulo_pacientes.py

import datetime
import time
import random
from modules.monticulo import MonticuloBinario
from modules.paciente import Paciente

class TriajePacientes:
    def __init__(self):
        self.monticulo = MonticuloBinario()

    def agregar_paciente(self, pac):
        # Inserta el paciente en el montículo usando el nivel de riesgo como clave. Para priorizar, insertamos una tupla (riesgo, paciente)
        self.monticulo.insertar((pac.get_riesgo(), pac))

    def atender_paciente(self):
        # Elimina y retorna el paciente con mayor prioridad de riesgo
        if self.monticulo.tam > 0:
            _, pac = self.monticulo.eliminarMin()
            return pac
        return None

    def pacientes_en_espera(self):
        # Devuelve la lista de pacientes restantes en espera (para visualizar)
        return [pac for _, pac in self.monticulo.lis_mon[1:]]

def simulacion(n,triaje):
    # Ciclo que gestiona la simulación
    for i in range(n):
        # Fecha y hora de entrada de un paciente
        ahora = datetime.datetime.now()
        fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
        print('-*-' * 15)
        print(f'\n{fecha_y_hora}\n')

        # Se crea un paciente y se agrega al montículo
        paciente = Paciente()
        triaje.agregar_paciente(paciente)
        print("Paciente ingresado:", paciente)

        # Atención de paciente en este ciclo: en el 50% de los casos
        if random.random() < 0.5:
            # Atiende al paciente con mayor prioridad de riesgo
            paciente_atendido = triaje.atender_paciente()
            if paciente_atendido:
                print('*' * 40)
                print('Se atiende el paciente:', paciente_atendido)
                print('*' * 40)

        # Se muestran los pacientes restantes en la cola de espera
        print('Pacientes que faltan atenderse:', len(triaje.pacientes_en_espera()))
        for paciente in triaje.pacientes_en_espera():
            print('\t', paciente)

        print('-*-' * 15)
        time.sleep(1)