from modules.clases import leer_archivo, mst_prim

# Especificar la ruta del archivo
ruta_archivo = "C:\\Users\\gjmor\\Downloads\\aldeas.txt"

# Leer las aldeas desde el archivo
try:
    aldeas = leer_archivo(ruta_archivo)
except Exception as e:
    print(f"Error al leer el archivo: {e}")
    exit()

# Verificar que la aldea "Peligros" esté en los datos
aldea_inicio = aldeas.get("Peligros")
if not aldea_inicio:
    print("La aldea 'Peligros' no existe en los datos.")
    exit()

# Calcular el árbol de expansión mínima
mst, total_distancia = mst_prim(aldeas, aldea_inicio)

# Mostrar la lista de aldeas en orden alfabético
aldeas_ordenadas = sorted(aldeas.keys())
print("Lista de aldeas en orden alfabético:")
for aldea in aldeas_ordenadas:
    print(aldea)

# Mostrar las conexiones eficientes entre aldeas
print("\nConexiones eficientes entre aldeas:")
for aldea1, aldea2, distancia in mst:
    print(f"{aldea1} envía noticia a {aldea2} (distancia: {distancia} leguas)")

# Mostrar la distancia total recorrida por las palomas
print(f"\nDistancia total recorrida por las palomas: {total_distancia} leguas")
