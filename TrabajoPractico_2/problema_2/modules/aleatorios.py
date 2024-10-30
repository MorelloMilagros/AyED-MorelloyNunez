import random
from datetime import datetime, timedelta
from modules.temp import Temperaturas_DB  # Asegúrate de que el nombre del archivo sea correcto.

def generar_fechas_temperaturas():
    db = Temperaturas_DB()
    fecha_inicial = datetime.now()
    temperaturas_generadas = []

    for i in range(50):
        fecha = fecha_inicial + timedelta(days=i)
        fecha_str = fecha.strftime("%d/%m/%Y")
        temperatura = round(random.uniform(-10, 40), 2)  # Genera una temperatura aleatoria
        db.guardar_temperatura(temperatura, fecha_str)  # Guarda en el sistema
        temperaturas_generadas.append((fecha_str, temperatura))

    return temperaturas_generadas  # Devuelve la lista para imprimirla luego en main

generar_fechas_temperaturas()
