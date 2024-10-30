# main.py
from modules.clases import leer_archivo, mst_prim  # Importar las funciones necesarias

arch = "data/aldeas.txt"

def mostrar_resultados(arbol, aldeas):
    # Ordenar aldeas alfabéticamente
    nombres_aldeas = sorted(aldeas.keys())
    print("Lista de Aldeas en orden alfabético:")
    for nombre in nombres_aldeas:
        print(nombre)

    print("\nRutas de envío de noticias:")
    for origen, destino, distancia in arbol.conexiones:
        print(f"Desde {origen} se envía a {destino} con distancia {distancia} leguas.")

    print(f"\nSuma total de distancias recorridas: {arbol.total_distancia} leguas.")

# Ejecución del código principal
if __name__ == "__main__":
    aldeas = leer_archivo(arch)  # Asegúrate de especificar la ruta correcta
    arbol = mst_prim(aldeas, aldeas['Peligros'])  # Peligros como aldea de inicio
    mostrar_resultados(arbol, aldeas)
