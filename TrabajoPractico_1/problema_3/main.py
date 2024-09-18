"""import sys
import os

# Agrega la carpeta padre al sys.path para que encuentre el módulo
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

from modules.clases import Juego

# El resto del código..."""

from modules.clases import Juego

# Inicializar el juego
juego = Juego()

# Jugar el juego
resultado = juego.jugar()

# Mostrar el resultado del juego
if resultado == 1:
    print("Jugador 1 gana el juego")
elif resultado == 2:
    print("Jugador 2 gana el juego")
else:
    print(f"El juego termina en empate después de {juego.N_TURNOS} turnos")
