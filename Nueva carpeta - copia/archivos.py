import csv

def load_csv(filename):
    products = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['precio'] = float(row['precio'])
                row['unidades_vendidas'] = int(row['unidades_vendidas'])
                row['stock'] = int(row['stock'])
                products.append(row)
        print("Archivo cargado con éxito.")
    except FileNotFoundError:
        print(f"Archivo {filename} no encontrado.")
    return products

def print_list(products):
    if not products:
        print("No hay datos cargados.")
        return
    print("{:<10} {:<20} {:<10} {:<20} {:<10}".format('ID', 'Producto', 'Precio', 'Unidades Vendidas', 'Stock'))
    for product in products:
        print("{:<10} {:<20} {:<10.2f} {:<20} {:<10}".format(product['id'], product['producto'], product['precio'], product['unidades_vendidas'], product['stock']))
