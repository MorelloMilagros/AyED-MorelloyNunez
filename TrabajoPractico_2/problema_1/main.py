from modules.colaprioridad import Cola_De_Prioridad
from modules.simulacro import simulacion

n = 20  # cantidad de ciclos de simulación

cola_de_espera = Cola_De_Prioridad()

simulacion(cola_de_espera, n)