import archivos
import estadisticas

import json
salir = False
def main():
    products = []
    while True:
        print("Menú:")
        print("1. Cargar archivo CSV")
        print("2. Imprimir lista")
        print("3. Actualizar estadísticas de ventas")
        print("4. Filtrar por productos más vendidos")
        print("5. Filtrar por bajo stock")
        print("6. Informar promedio de precio")
        print("7. Ordenar datos por nombre de producto ascendente")
        print("8. Mostrar producto más vendido")
        print("9. Salir")
        seleccion = input("Seleccione una opción: ")

        if seleccion == '1':
            filename = input("Ingrese el nombre del archivo CSV: ")
            products = archivos.cargar_csv(filename)
        elif seleccion == '2':
            archivos.cargar_lista(products)
        elif seleccion == '3':
            products = estadisticas.actualizar_ventas(products)
        elif seleccion == '4':
            filename = input("Ingrese el nombre del archivo para guardar los productos más vendidos: ")
            estadisticas.mas_vendido(products, filename)
        elif seleccion == '5':
            filename = input("Ingrese el nombre del archivo para guardar los productos con bajo stock: ")
            estadisticas.menos_stock(products, filename)
        elif seleccion == '6':
            avg_price = estadisticas.precio_promedio(products)
            print(f"El precio promedio de los productos es: {avg_price:.2f}")
        elif seleccion == '7':
            print("nada")
        elif seleccion == '8':
            product, units_sold = estadisticas.mas_vendido(products)
            print(f"El producto más vendido es '{product}' con {units_sold} unidades vendidas.")
        elif seleccion == '9':
            salir = True
            return salir
        else:
            print("Opción no válida, intente de nuevo.")


while salir == False:
    salir = main()