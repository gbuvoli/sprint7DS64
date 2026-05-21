from misfunciones import calcular_total, aplicar_descuento


print("Hello, World!")
print("Welcome to the world of programming!")

# Ejemplo de uso de las funciones
precio = 10
cantidad = 5
descuento = 0.2

total = calcular_total(precio, cantidad)
print(f"Total sin descuento: {total}")

total_con_descuento = aplicar_descuento(total, descuento)
print(f"Total con descuento: {total_con_descuento}")