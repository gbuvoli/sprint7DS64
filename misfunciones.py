#Creare mis propias funciones para utilizarlas en el futuro o en mi proyecto.

def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total


def aplicar_descuento(total, descuento):
    valor_descuento = total * descuento
    total_con_descuento = total - valor_descuento
    return total_con_descuento