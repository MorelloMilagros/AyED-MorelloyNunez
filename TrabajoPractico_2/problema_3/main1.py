# main.py
from modules_op1.prim import leer_archivo, mst_prim, mostrar_resultados

arch = "data/aldeas.txt"

if __name__ == "__main__":
    aldeas = leer_archivo(arch)
    arbol = mst_prim(aldeas, aldeas['Peligros'])
    mostrar_resultados(arbol, aldeas)
