import archivos
import estadisticas
import ordenamiento
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
        choice = input("Seleccione una opción: ")

        if choice == '1':
            filename = input("Ingrese el nombre del archivo CSV: ")
            products = archivos.load_csv(filename)
        elif choice == '2':
            archivos.print_list(products)
        elif choice == '3':
            products = estadisticas.update_sales_stats(products)
        elif choice == '4':
            filename = input("Ingrese el nombre del archivo para guardar los productos más vendidos: ")
            estadisticas.filter_most_sold(products, filename)
        elif choice == '5':
            filename = input("Ingrese el nombre del archivo para guardar los productos con bajo stock: ")
            estadisticas.filter_low_stock(products, filename)
        elif choice == '6':
            avg_price = estadisticas.calculate_average_price(products)
            print(f"El precio promedio de los productos es: {avg_price:.2f}")
        elif choice == '7':
            sorted_products = ordenamiento.sort_by_product_name(products)
            with open('productos_ordenados.json', 'w') as f:
                json.dump(sorted_products, f, indent=4)
            print("Datos ordenados y guardados en 'productos_ordenados.json'.")
        elif choice == '8':
            product, units_sold = estadisticas.most_sold_product(products)
            print(f"El producto más vendido es '{product}' con {units_sold} unidades vendidas.")
        elif choice == '9':
            salir = True
            return salir
        else:
            print("Opción no válida, intente de nuevo.")

#if __name__ == "__main__":
#    main()
while salir == False:
    salir = main()