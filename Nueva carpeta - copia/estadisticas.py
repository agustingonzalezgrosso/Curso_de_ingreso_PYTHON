import random

def update_sales_stats(products):
    for product in products:
        product['unidades_vendidas'] = random.randint(1, 100)
        product['stock'] = random.randint(50, 300)
    print("Estadísticas de ventas actualizadas.")
    return products

def filter_most_sold(products, filename):
    most_sold = [p for p in products if p['unidades_vendidas'] > 50]
    with open(filename, 'w') as file:
        for product in most_sold:
            file.write(f"{product['id']},{product['producto']},{product['precio']},{product['unidades_vendidas']},{product['stock']}\n")
    print(f"Productos más vendidos guardados en {filename}.")

def filter_low_stock(products, filename):
    low_stock = [p for p in products if p['stock'] < 20]
    with open(filename, 'w') as file:
        for product in low_stock:
            file.write(f"{product['id']},{product['producto']},{product['precio']},{product['unidades_vendidas']},{product['stock']}\n")
    print(f"Productos con bajo stock guardados en {filename}.")

def calculate_average_price(products):
    if not products:
        return 0
    total_price = sum(p['precio'] for p in products)
    return total_price / len(products)

def most_sold_product(products):
    if not products:
        return None, 0
    most_sold = max(products, key=lambda p: p['unidades_vendidas'])
    return most_sold['producto'], most_sold['unidades_vendidas']
