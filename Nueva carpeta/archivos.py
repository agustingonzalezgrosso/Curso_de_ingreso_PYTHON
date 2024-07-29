import csv

def cargar_csv(nombre_archivo):
    products = []
    try:
        with open(nombre_archivo, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['precio'] = float(row['precio'])
                row['unidades_vendidas'] = int(row['unidades_vendidas'])
                row['stock'] = int(row['stock'])
                products.append(row)
        print("Archivo cargado con éxito.")
    except FileNotFoundError:
        print(f"Archivo {nombre_archivo} no encontrado.")
    return products

def cargar_lista(products):
    if not products:
        print("No hay datos cargados.")
        return
    print(('ID', 'Producto', 'Precio', 'Unidades Vendidas', 'Stock'))
    for producto in products:
        print((producto['id'], producto['producto'], producto['precio'], producto['unidades_vendidas'], producto['stock']))
