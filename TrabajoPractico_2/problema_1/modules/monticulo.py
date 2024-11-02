class MonticuloMin:
    def __init__(self):
        self._datos = []

    def insertar(self, elemento):
        # Insertar elemento al final y ajustar el montículo hacia arriba
        self._datos.append(elemento)
        self._subir(len(self._datos) - 1)

    def extraer_min(self):
        # Si está vacío, no hacer nada
        if len(self._datos) == 0:
            return None
        # Intercambiar el mínimo con el último elemento
        min_elemento = self._datos[0]
        ultimo_elemento = self._datos.pop()
        if len(self._datos) > 0:
            self._datos[0] = ultimo_elemento
            self._bajar(0)
        return min_elemento

    def obtener_elementos(self):
        # Devolver una lista de los elementos actuales en el montículo
        return list(self._datos)

    def _subir(self, indice):
        # Ajusta el elemento en `indice` hacia arriba según la prioridad
        while indice > 0:
            padre = (indice - 1) // 2
            if (self._datos[indice].get_riesgo(), self._datos[indice].orden_llegada) < \
               (self._datos[padre].get_riesgo(), self._datos[padre].orden_llegada):
                self._datos[indice], self._datos[padre] = self._datos[padre], self._datos[indice]
                indice = padre
            else:
                break

    def _bajar(self, indice):
        # Ajusta el elemento en `indice` hacia abajo según la prioridad
        longitud = len(self._datos)
        while True:
            hijo_izq = 2 * indice + 1
            hijo_der = 2 * indice + 2
            min_indice = indice

            if hijo_izq < longitud and \
               (self._datos[hijo_izq].get_riesgo(), self._datos[hijo_izq].orden_llegada) < \
               (self._datos[min_indice].get_riesgo(), self._datos[min_indice].orden_llegada):
                min_indice = hijo_izq

            if hijo_der < longitud and \
               (self._datos[hijo_der].get_riesgo(), self._datos[hijo_der].orden_llegada) < \
               (self._datos[min_indice].get_riesgo(), self._datos[min_indice].orden_llegada):
                min_indice = hijo_der

            if min_indice == indice:
                break

            self._datos[indice], self._datos[min_indice] = self._datos[min_indice], self._datos[indice]
            indice = min_indice
    def __len__(self):
        return len(self._datos)
