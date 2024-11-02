from modules.temp import Temperaturas_DB

from modules.aleatorios import generar_fechas_temperaturas

# Genera y muestra temperaturas
temperaturas , db= generar_fechas_temperaturas()
print("Fechas y temperaturas generadas:")
for fecha, temp in temperaturas:
    print(f"Fecha: {fecha}, Temperatura: {temp}°C")

def menu():
    print("\nMenú de opciones:")
    print("1. Guardar temperatura")
    print("2. Devolver temperatura")
    print("3. Máxima temperatura en rango")
    print("4. Mínima temperatura en rango")
    print("5. Extremos de temperatura en rango")
    print("6. Borrar temperatura")
    print("7. Devolver temperaturas en rango")
    print("8. Cantidad de muestras")
    print("9. Salir")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            fecha = input("Ingrese la fecha (dd/mm/aaaa): ")
            temperatura_input = input("Ingrese la temperatura (solo el numero): ")
            # Excepción: reemplazar la coma por un punto en temperaturas
            temperatura_input = temperatura_input.replace(",", ".")
            temperatura = float(temperatura_input)
            db.guardar_temperatura(temperatura, fecha)
            print("Temperatura guardada.")
        
        elif opcion == "2":
            fecha = input("Ingrese la fecha (dd/mm/aaaa): ")
            try:
                temp = db.devolver_temperatura(fecha)
                print(f"La temperatura registrada el {fecha} es: {temp} ºC")
            except ValueError:
                print("La fecha ingresada no tienen ninguna temperatura registrada")
        
        elif opcion == "3":
            fecha1 = input("Ingrese la fecha de inicio del rango(dd/mm/aaaa): ")
            fecha2 = input("Ingrese la fecha de fin del rango(dd/mm/aaaa): ")
            try:
                max_temp = db.max_temp_rango(fecha1, fecha2)
                print(f"La temperatura máxima entre {fecha1} y {fecha2} es: {max_temp} ºC")
            except ValueError:
                print("No hay temperaturas guardadas en el rango ingresado")
        
        elif opcion == "4":
            fecha1 = input("Ingrese la fecha de inicio del rango(dd/mm/aaaa): ")
            fecha2 = input("Ingrese la fecha de fin del rango(dd/mm/aaaa): ")
            try:
                min_temp = db.min_temp_rango(fecha1, fecha2)
                print(f"La temperatura mínima entre {fecha1} y {fecha2} es: {min_temp} ºC")
            except ValueError:
                print("No hay temperaturas guardadas en el rango ingresado")
        
        elif opcion == "5":
            fecha1 = input("Ingrese la fecha de inicio (dd/mm/aaaa): ")
            fecha2 = input("Ingrese la fecha de fin (dd/mm/aaaa): ")
            try:
                min_temp, max_temp = db.temp_extremos_rango(fecha1, fecha2)
                print(f"Las temperaturas extremas entre {fecha1} y {fecha2} son: mínima {min_temp} ºC, máxima {max_temp} ºC")
            except ValueError:
                print("El rango ingresado es incorrecto, o no hay temperaturas ingresadas en ese rango")
        
        elif opcion == "6":
            fecha = input("Ingrese la fecha (dd/mm/aaaa): ")
            try:
                db.borrar_temperatura(fecha)
                print(f"Temperatura del {fecha} eliminada.")
            except ValueError:
                print("La fecha ingresada no tienen ninguna temperatura registrada")
        
        elif opcion == "7":
            fecha1 = input("Ingrese la fecha de inicio (dd/mm/aaaa): ")
            fecha2 = input("Ingrese la fecha de fin (dd/mm/aaaa): ")
            temperaturas = db.devolver_temperaturas(fecha1, fecha2)
            if temperaturas:
                print("\nTemperaturas registradas en el rango:")
                for temp in temperaturas:
                    print(temp)
            else:
                print(f"No hay temperaturas registradas entre {fecha1} y {fecha2}.")
        
        elif opcion == "8":
            print(f"Cantidad de muestras registradas: {db.cantidad_muestras()}")
        
        elif opcion == "9":
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
