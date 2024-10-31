from modules_op1.monticulo import MonticuloBinario

class ColaPrioridad:
    def __init__(self):
        self.monticulo = MonticuloBinario()  # Utiliza MonticuloBinario para almacenar los elementos
        self.posiciones = {}  # Diccionario para rastrear posiciones de los objetos en el montículo

    def construirMonticulo(self, lista):
        # Recibe una lista de tuplas (clave, objeto) y construye el montículo
        self.monticulo.construirMonticulo(lista)
        for i, (_, obj) in enumerate(self.monticulo.lis_mon[1:], start=1):
            self.posiciones[obj] = i  # Almacena la posición del objeto

    def insertar(self, clave, obj):
        # Inserta una tupla (clave, objeto) en el montículo y actualiza las posiciones
        self.monticulo.insertar((clave, obj))
        self.posiciones[obj] = self.monticulo.tam

    def eliminarMin(self):
        # Extrae el elemento con la mínima clave y actualiza las posiciones
        clave, obj = self.monticulo.eliminarMin()
        self.posiciones.pop(obj, None)
        return clave, obj

    def decrementarClave(self, obj, nueva_clave):
        index = None
        # Busca el índice del objeto en el montículo
        for i in range(1, len(self.monticulo.lis_mon)):
            if self.monticulo.lis_mon[i][1] == obj:
                index = i
                break

        # Si el índice se encuentra y la nueva clave es menor, actualiza
        if index is not None and nueva_clave < self.monticulo.lis_mon[index][0]:
            self.monticulo.lis_mon[index] = (nueva_clave, obj)
            self.monticulo.infiltArriba(index)

    def estaVacia(self):
        return self.monticulo.tam == 0

    def contiene(self, obj):
        # Verifica si el objeto está en la cola de prioridad
        return obj in self.posiciones