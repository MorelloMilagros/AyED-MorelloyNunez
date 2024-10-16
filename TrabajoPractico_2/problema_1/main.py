# main.py

import datetime
import time
import random
from modules.paciente import Paciente
from modules.mont_pacientes import TriajePacientes

n = 20  # Cantidad de ciclos de simulación

# Crear el gestor de triaje con el montículo
triaje = TriajePacientes()

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
