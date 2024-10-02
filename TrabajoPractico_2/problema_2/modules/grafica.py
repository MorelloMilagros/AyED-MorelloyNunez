import time
import matplotlib.pyplot as plt
from lista_doble_enlazada import ListaDobleEnlazada

def medir_tiempo(func, *args):
    inicio = time.time()
    func(*args)
    fin = time.time()
    return fin - inicio

# Crear listas con diferentes tamaños
tamanios = [100, 500, 1000, 5000, 10000, 20000]
tiempos_len = []
tiempos_copiar = []
tiempos_invertir = []

for n in tamanios:
    lde = ListaDobleEnlazada()
    for i in range(n):
        lde.agregar_al_final(i)

    # Medir tiempo para len
    tiempo_len = medir_tiempo(len, lde)
    tiempos_len.append(tiempo_len)

    # Medir tiempo para copiar
    tiempo_copiar = medir_tiempo(lde.copiar)
    tiempos_copiar.append(tiempo_copiar)

    # Medir tiempo para invertir
    tiempo_invertir = medir_tiempo(lde.invertir)
    tiempos_invertir.append(tiempo_invertir)

# Graficar los resultados
plt.figure(figsize=(10, 6))
plt.plot(tamanios, tiempos_len, label='len', marker='o')
plt.plot(tamanios, tiempos_copiar, label='copiar', marker='o')
plt.plot(tamanios, tiempos_invertir, label='invertir', marker='o')
plt.xlabel('Cantidad de Elementos (N)')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.title('N vs Tiempo de Ejecución')
plt.legend()
plt.grid(True)
plt.show()