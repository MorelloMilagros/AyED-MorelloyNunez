from datetime import datetime
from modules.arbol_avl import AVLTree

class Temperaturas_DB:
    def __init__(self):
        self.arbol = AVLTree()
        self.raiz = None
        self.muestras = 0

    def guardar_temperatura(self, temperatura, fecha_str):
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        self.raiz = self.arbol.insertar(self.raiz, fecha, temperatura)
        self.muestras += 1

    def devolver_temperatura(self, fecha_str):
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        return self.arbol.buscar(self.raiz, fecha)

    def max_temp_rango(self, fecha1_str, fecha2_str):
        fecha1 = datetime.strptime(fecha1_str, "%d/%m/%Y")
        fecha2 = datetime.strptime(fecha2_str, "%d/%m/%Y")
        resultados = []
        self.arbol.inorden_rango(self.raiz, fecha1, fecha2, resultados)
        return max(resultados, key=lambda x: x[1])[1]

    def min_temp_rango(self, fecha1_str, fecha2_str):
        fecha1 = datetime.strptime(fecha1_str, "%d/%m/%Y")
        fecha2 = datetime.strptime(fecha2_str, "%d/%m/%Y")
        resultados = []
        self.arbol.inorden_rango(self.raiz, fecha1, fecha2, resultados)
        return min(resultados, key=lambda x: x[1])[1]

    def temp_extremos_rango(self, fecha1_str, fecha2_str):
        fecha1 = datetime.strptime(fecha1_str, "%d/%m/%Y")
        fecha2 = datetime.strptime(fecha2_str, "%d/%m/%Y")
        resultados = []
        self.arbol.inorden_rango(self.raiz, fecha1, fecha2, resultados)
        return min(resultados, key=lambda x: x[1])[1], max(resultados, key=lambda x: x[1])[1]

    def borrar_temperatura(self, fecha_str):
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        self.raiz = self.arbol.eliminar(self.raiz, fecha)
        self.muestras -= 1

    def devolver_temperaturas(self, fecha1_str, fecha2_str):
        fecha1 = datetime.strptime(fecha1_str, "%d/%m/%Y")
        fecha2 = datetime.strptime(fecha2_str, "%d/%m/%Y")
        resultados = []
        self.arbol.inorden_rango(self.raiz, fecha1, fecha2, resultados)
        return [f"{fecha.strftime('%d/%m/%Y')}: {temp} ºC" for fecha, temp in resultados]

    def cantidad_muestras(self):
        return self.muestras
