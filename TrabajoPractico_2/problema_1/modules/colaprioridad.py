from monticulo import MonticuloMin

class Cola_De_Prioridad:
    def __init__(self):
        self._monticulo = MonticuloMin()
        self._orden_llegada = 0

    def append(self, paciente):
        # Asignar orden de llegada al paciente
        paciente.orden_llegada = self._orden_llegada
        self._orden_llegada += 1
        # Insertar paciente en el montículo
        self._monticulo.insertar(paciente)

    def pop(self):
        # Extraer paciente de mayor prioridad (menor riesgo numérico)
        return self._monticulo.extraer_min()

    def __len__(self):
        # Retornar la cantidad de pacientes en la cola
        return len(self._monticulo)
    
    def __iter__(self):
        # Crear un iterador sobre los elementos en el montículo
        return iter(self._monticulo.obtener_elementos())
