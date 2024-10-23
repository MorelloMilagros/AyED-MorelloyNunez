from modules.triaje_p import TriajePacientes, simulacion

n = 20  # Cantidad de ciclos de simulación

# Crear el gestor de triaje con el montículo
triaje = TriajePacientes()

simulacion(n, triaje)