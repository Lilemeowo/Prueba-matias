import random
import math

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]


def asignar_sueldos():
    sueldos = []
    for _ in range(10):
        sueldo = random.randint(300000, 2500000)
        sueldos.append(sueldo)
    return sueldos

sueldos = asignar_sueldos()
def clasificar_sueldos(trabajadores, sueldos):
    menores = []
    medios = []
    mayores = []
    
    for i in range(len(sueldos)):
        if sueldos[i] < 800000:
            menores.append((trabajadores[i], sueldos[i]))
        elif sueldos[i] <= 2000000:
            medios.append((trabajadores[i], sueldos[i]))
        else:
            mayores.append((trabajadores[i], sueldos[i]))
    
    print("Sueldos menores a $800.000")
    for empleado in menores:
        print(f"{empleado[0]}: ${empleado[1]}")
    print(f"TOTAL: {len(menores)}\n")

    print("Sueldos entre $800.000 y $2.000.000")
    for empleado in medios:
        print(f"{empleado[0]}: ${empleado[1]}")
    print(f"TOTAL: {len(medios)}\n")

    print("Sueldos superiores a $2.000.000")
    for empleado in mayores:
        print(f"{empleado[0]}: ${empleado[1]}")
    print(f"TOTAL: {len(mayores)}\n")

    total_sueldos = sum(sueldos)
    print(f"TOTAL SUELDOS: ${total_sueldos}\n")


def ver_estadisticas(sueldos):
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    promedio = sum(sueldos) / len(sueldos)
    media_geometrica =(sum(sueldos)/10)
    
    
    
    
    print(f"Sueldo más alto: ${sueldo_max}")
    print(f"Sueldo más bajo: ${sueldo_min}")
    print(f"Promedio de sueldos: ${promedio}")
    print(f"Media geométrica de sueldos: ${media_geometrica}\n")

def reporte_sueldos(trabajadores, sueldos):
    with open("reporte_sueldos.csv", "w") as file:
        file.write("Nombre empleado,Sueldo Base,Descuento Salud,Descuento AFP,Sueldo Líquido\n")
        for i in range(len(sueldos)):
            descuento_salud = sueldos[i] * 0.07
            descuento_afp = sueldos[i] * 0.12
            sueldo_liquido = sueldos[i] - descuento_salud - descuento_afp
            file.write(f"{trabajadores[i]},{sueldos[i]},{descuento_salud},{descuento_afp},{sueldo_liquido}\n")

    print("Reporte de sueldos generado en 'reporte_sueldos.csv'\n")

def menu():
    sueldos = []
    while True:
        print("Menú de opciones:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            sueldos = asignar_sueldos()
            print("Sueldos asignados.\n")
        elif opcion == "2":
            if sueldos:
                clasificar_sueldos(trabajadores, sueldos)
            else:
                print("Primero asigne los sueldos.\n")
        elif opcion == "3":
            if sueldos:
                ver_estadisticas(sueldos)
            else:
                print("Primero asigne los sueldos.\n")
        elif opcion == "4":
            if sueldos:
                reporte_sueldos(trabajadores, sueldos)
            else:
                print("Primero asigne los sueldos.\n")
        elif opcion == "5":
            print("Finalizando programa...\nDesarrollado por Matias Pulgar\nRUT 20.395.040-3")
            break
        else:
            print("Opción no válida, intente nuevamente.\n")


menu()
