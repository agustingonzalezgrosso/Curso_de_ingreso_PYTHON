import random

def actualizar_ventas(products):
    for producto in products:
        producto['unidades_vendidas'] = random.randint(1, 100)
        producto['stock'] = random.randint(50, 300)
    print("Estadísticas de ventas actualizadas.")
    return products

def mas_vendido(products, nombre_archivo):
    mas_ventas = [p for p in products if p['unidades_vendidas'] > 50]
    with open(nombre_archivo, 'w') as file:
        for producto in mas_ventas:
            file.write(f"{producto['id']},{producto['producto']},{producto['precio']},{producto['unidades_vendidas']},{producto['stock']}\n")
    print(f"Productos más vendidos guardados en {nombre_archivo}.")

def menos_stock(products, nombre_archivo):
    menor_stock = [p for p in products if p['stock'] < 20]
    with open(nombre_archivo, 'w') as file:
        for producto in menor_stock:
            file.write(f"{producto['id']},{producto['producto']},{producto['precio']},{producto['unidades_vendidas']},{producto['stock']}\n")
    print(f"Productos con bajo stock guardados en {nombre_archivo}.")

def precio_promedio(products):
    if not products:
        return 0
    precio_total = sum(p['precio'] for p in products)
    return precio_total / len(products)

def mas_vendido(products):
    if not products:
        return None, 0
    mas_ventas = max(products, key=lambda p: p['unidades_vendidas'])
    return mas_ventas['producto'], mas_ventas['unidades_vendidas']
