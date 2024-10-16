Palomas mensajeras - Optimización del envío de noticias

Introducción:

Nos enfrentamos al reto de optimizar el envío de noticias usando palomas mensajeras desde la aldea de Peligros hacia otras 21 aldeas vecinas. Nuestro objetivo es minimizar la distancia total recorrida, asegurando que cada aldea reciba la noticia una sola vez y luego la reenvíe a las aldeas más cercanas.

Solución:

Utilizamos el algoritmo de Prim para encontrar la mejor manera de conectar todas las aldeas con la menor distancia posible. A partir del archivo aldeas.txt, que contiene las conexiones y distancias entre las aldeas, creamos un grafo donde las aldeas son nodos y las distancias son las rutas que recorren las palomas.

Resultados:

El programa genera tres resultados principales:

Lista de aldeas en orden alfabético: Incluye aldeas como Aceituna, Buenas Noches, Lomaseca, Peligros, entre otras.

Conexiones eficientes entre aldeas: Por ejemplo, Peligros envía noticias a Lomaseca (7 leguas), y Lomaseca las reenvía a Los Infiernos (2 leguas).

Distancia total recorrida: Las palomas recorren un total de XX leguas.

Conclusión:

El algoritmo de Prim nos permitió encontrar la manera más eficiente de distribuir las noticias, reduciendo el esfuerzo y la distancia recorrida por las palomas. Gracias a este enfoque, la agencia "Palomas William" puede enviar las noticias de manera rápida y optimizada.