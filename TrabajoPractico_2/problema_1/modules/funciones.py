import random
import time
from modules.clases import llegada_paciente, atender_paciente, obtener_pacientes_en_espera, listar_pacientes

# Cola de prioridad para gestionar pacientes
cola_prioridad = []

# Simulación de triaje en sala de emergencias
def simulacion_triaje(n):
    for i in range(n):
        nombre_paciente = f"Paciente_{i+1}"
        riesgo_paciente = random.randint(1, 3)  # Niveles de riesgo: 1 (crítico), 2 (moderado), 3 (bajo)
        paciente = llegada_paciente(cola_prioridad, nombre_paciente, riesgo_paciente)
        print(f"Llegó {paciente}")
        
        if random.random() < 0.5:
            paciente_atendido = atender_paciente(cola_prioridad)
            if paciente_atendido:
                print(f"Atendiendo a {paciente_atendido}")
            else:
                print("No hay pacientes para atender.")
        
        print(f"Pacientes en espera: {obtener_pacientes_en_espera(cola_prioridad)}")
        for paciente in listar_pacientes(cola_prioridad):
            print(f"  {paciente}")
        print('-'*40)

        time.sleep(1)
