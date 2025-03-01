#Data quemada, Diccionario
productos = {
    1: {"Nombre": "Manzana", "precio": 1.5, "stock": 100},
    2: {"Nombre": "Platano", "precio": 1.0, "stock": 110},
    3: {"Nombre": "Pera", "precio": 2.0, "stock": 80},
    4: {"Nombre": "Uva", "precio": 2.5, "stock": 70},
    5: {"Nombre": "Sandia", "precio": 3.0, "stock": 100},
    6: {"Nombre": "Melon", "precio": 2.8, "stock": 100},
    7: {"Nombre": "Naranja", "precio": 1.2, "stock": 100},
    8: {"Nombre": "Mandarina", "precio": 1.3, "stock": 90},
    9: {"Nombre": "kiwi", "precio": 3.5, "stock": 50},
    10: {"Nombre": "Fresa", "precio": 2.8, "stock": 60},
    11: {"Nombre": "Aguacate", "precio": 2.2, "stock": 106},
    12: {"Nombre": "Papaya", "precio": 2.6, "stock": 110},
    13: {"Nombre": "Granadilla", "precio": 3.2, "stock": 100},
    14: {"Nombre": "Cereza", "precio": 4.0, "stock": 100},
    15: {"Nombre": "Franbuesa", "precio": 3.7, "stock": 50},
    16: {"Nombre": "Platano macho", "precio": 1.8, "stock": 110},
    17: {"Nombre": "Piña", "precio": 3.5, "stock": 110},
    18: {"Nombre": "Mango", "precio": 2.5, "stock": 100},
    19: {"Nombre": "Lima", "precio": 1.0, "stock": 70},
    20: {"Nombre": "Limon", "precio": 1.0, "stock": 40},
}

#lista historial de ventas 
historial_ventas = []

def obtener_producto(id_producto):
    """Retornar los datos del producto de acuerdo a su ID"""
    return productos.get(id_producto, None)

def calcular_total(lista_productos):
    """Calcular el total de la compra """
    total = 0
    for producto in lista_productos:
        total += producto['precio']
    return total

def agregar_producto(id_producto, cantidad, lista_productos):
    """Agregar un producto a lista de compra y registrar la venta"""
    producto = obtener_producto(id_producto)
    if producto: 
        lista_productos.append({"nombre": producto["nombre"], "precio": producto["precio"]* cantidad})

        #Registrar la venta en el hidtorial
        historial_ventas.append({
            "producto": producto["nombre"],
            "cantidad": cantidad,
            "precio total": producto["precio"] * cantidad
        })
    else: 
        raise ValueError(f"Producto con Id {id_producto} no encontrado")

