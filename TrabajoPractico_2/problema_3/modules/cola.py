from modules.monticulo import MonticuloBinario

class ColaPrioridad:
    def __init__(self):
        self.monticulo = MonticuloBinario()  # Utiliza MonticuloBinario para almacenar los elementos
        self.posiciones = {}  # Diccionario para rastrear posiciones de los objetos en el montículo
        self.elementos = set()

    def construirMonticulo(self, lista):
        self.monticulo.construirMonticulo(lista)  # Llama al método de construcción en MonticuloBinario
        self.elementos = {v for _, v in lista}

    def insertar(self, clave, obj):
        # Inserta una tupla (clave, objeto) en el montículo y actualiza las posiciones
        self.monticulo.insertar((clave, obj))
        self.posiciones[obj] = self.monticulo.tam

    def eliminarMin(self):
        min_elemento = self.monticulo.eliminarMin()  # Obtener el mínimo del MonticuloBinario
        self.elementos.remove(min_elemento[1])  # Remueve el vértice del conjunto
        return min_elemento

    def decrementarClave(self, obj, nueva_clave):
        # Decrementa la clave del objeto y ajusta el montículo
        index = self.posiciones.get(obj)
        if index is not None and nueva_clave < self.monticulo.lis_mon[index][0]:
            self.monticulo.lis_mon[index] = (nueva_clave, obj)  # Actualiza la clave en la posición actual
            self.monticulo.infiltArriba(index)  # Ajusta hacia arriba
            # Actualiza la posición del objeto en el diccionario de posiciones
            self.posiciones[obj] = index

    def estaVacia(self):
        return self.monticulo.tam == 0

    def contiene(self, item):
        return item in self.elementos