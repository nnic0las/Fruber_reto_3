from productos import obtener_producto

def calcular_total(lista_productos):
    """Calcular el total de la compra"""
    total = 0
    for producto in lista_productos:
        total += producto['precio']
        return total
    
def agregar_producto(id_producto, cantidad, lista_productos):
    """Agregar un producto a la lista de compra"""
    producto = obtener_producto(id_producto)
    if producto:
        lista_productos.append({"nombre": producto["nombre"], "precio": producto["precio"]* cantidad})
