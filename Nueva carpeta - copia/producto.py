# Creamos el archivo CSV con los datos de ejemplo
import csv

productos = [
    {"id": 1, "producto": "camiseta", "precio": 20.0, "unidades_vendidas": 100, "stock": 50},
    {"id": 2, "producto": "pantalon", "precio": 25.0, "unidades_vendidas": 200, "stock": 150},
    {"id": 3, "producto": "chaqueta", "precio": 50.0, "unidades_vendidas": 50, "stock": 10},
    {"id": 4, "producto": "zapatos", "precio": 35.0, "unidades_vendidas": 75, "stock": 20},
    {"id": 5, "producto": "bufanda", "precio": 15.0, "unidades_vendidas": 10, "stock": 5},
]

with open('productos.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["id", "producto", "precio", "unidades_vendidas", "stock"])
    writer.writeheader()
    writer.writerows(productos)

print("Archivo 'productos.csv' creado con éxito.")
