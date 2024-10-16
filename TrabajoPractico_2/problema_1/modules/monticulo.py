class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo = [0]  # Inicializa el montículo con un 0 al inicio
        self.tamanoActual = 0  # Tamaño actual del montículo

    def infiltArriba(self, i):
        while i // 2 > 0:
            if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
                # Intercambia el valor con el padre si es menor
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            i = i // 2  # Mueve el índice al nodo padre

    def insertar(self, k):
        self.listaMonticulo.append(k)  # Añade el nuevo elemento al final
        self.tamanoActual += 1
        self.infiltArriba(self.tamanoActual)  # Ajusta el montículo hacia arriba

    def infiltAbajo(self, i):
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)  # Encuentra el hijo mínimo
            if self.listaMonticulo[i] > self.listaMonticulo[hm]:
                # Intercambia el valor con el hijo mínimo si es mayor
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm  # Mueve el índice al hijo mínimo

    def hijoMin(self, i):
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i * 2] < self.listaMonticulo[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def eliminarMin(self):
        valorSacado = self.listaMonticulo[1]  # El mínimo es el primer elemento
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual -= 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)  # Ajusta el montículo hacia abajo
        return valorSacado

    def construirMonticulo(self, unaLista):
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [0] + unaLista[:]
        while i > 0:
            self.infiltAbajo(i)
            i -= 1
