import heapq
import datetime

# Clase Paciente que contendrá el nivel de riesgo y la hora de llegada
class Paciente:
    def __init__(self, nombre, riesgo):
        self.nombre = nombre
        self.riesgo = riesgo
        self.hora_de_llegada = datetime.datetime.now()

    def __repr__(self):
        return f"Paciente(nombre={self.nombre}, riesgo={self.riesgo}, llegada={self.hora_de_llegada.strftime('%H:%M:%S')})"

# Función para comparar pacientes (por riesgo y luego por hora de llegada)
def comparar_pacientes(paciente):
    # Priorizar riesgo más bajo, luego la hora de llegada más temprana
    return (paciente.riesgo, paciente.hora_de_llegada)

# Función para añadir un paciente a la cola de prioridad
def llegada_paciente(cola_prioridad, nombre, riesgo):
    paciente = Paciente(nombre, riesgo)
    heapq.heappush(cola_prioridad, (comparar_pacientes(paciente), paciente))
    return paciente

# Función para atender pacientes según su prioridad
def atender_paciente(cola_prioridad):
    if cola_prioridad:
        _, paciente_atendido = heapq.heappop(cola_prioridad)
        return paciente_atendido
    else:
        return None

# Función para obtener el número de pacientes en espera
def obtener_pacientes_en_espera(cola_prioridad):
    return len(cola_prioridad)

# Función para obtener la lista de pacientes en espera
def listar_pacientes(cola_prioridad):
    # Ordenar por prioridad sin alterar el heap
    return sorted([paciente for _, paciente in cola_prioridad], key=lambda x: (x.riesgo, x.hora_de_llegada))
