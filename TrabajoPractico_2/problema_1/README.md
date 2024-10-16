Selección de la Estructura de Datos
Para el desarrollo de este proyecto, junto con mi compañera, decidimos utilizar una cola de prioridad como la estructura de datos más adecuada para manejar el triaje de pacientes en la sala de emergencias. La cola de prioridad nos permite asegurarnos de que siempre atendamos primero a los pacientes con mayor nivel de riesgo, lo cual es crucial para este tipo de simulaciones donde el tiempo y el riesgo clínico son factores clave.


Justificación de la Estructura
Optamos por la cola de prioridad porque es una estructura que permite insertar elementos con una prioridad asociada y, cuando se extrae un elemento, este siempre es el que tiene la prioridad más alta. En nuestro caso, los pacientes con un nivel de riesgo crítico (valor numérico más bajo) son los que tienen la mayor prioridad, mientras que aquellos con riesgos menores (valores numéricos más altos) se atienden después.


Para los casos donde dos pacientes tienen el mismo nivel de riesgo, usamos un criterio adicional para decidir el orden de atención: el orden de llegada. Esto lo logramos implementando un contador o marca temporal que nos permite mantener la secuencia en que fueron ingresando los pacientes.


Complejidad Algorítmica
En cuanto al análisis de eficiencia, la inserción de un paciente en la cola de prioridad tiene una complejidad de O(log n), donde n representa la cantidad de pacientes en la cola en ese momento. Esto se debe a la necesidad de reorganizar la cola para mantener el orden según la prioridad. La extracción del paciente más crítico también tiene una complejidad de O(log n), ya que al eliminar un paciente debemos reordenar la estructura para mantener la prioridad correcta entre los pacientes restantes.


Comparada con otras estructuras como una lista o una cola regular, la cola de prioridad es mucho más eficiente para el triaje, ya que no necesitamos recorrer toda la lista para encontrar al paciente más crítico.


Implementación
Hemos diseñado la cola de prioridad de manera genérica, de modo que pueda almacenar cualquier tipo de dato, no solo pacientes, lo que la hace más flexible y adaptable para futuros usos. La implementación interna de la cola de prioridad está basada en un heap binario, que es una de las formas más eficientes de manejar prioridades, garantizando tanto inserciones como eliminaciones en tiempos óptimos.


Por último, nos aseguramos de que la lógica del triaje esté separada de la implementación de la estructura de datos, para mantener un código modular y fácil de mantener en el futuro.
