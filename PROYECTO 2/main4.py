"""Vamos a crear una aplicación simulando la aplicación de un cajero de inventario de productos de una papelería, la idea es que tenga un carrito de compras y al final genere un recibo y guarde el historial de venta"""

productos = [
    {"nombre" : "lapiz", "precio" : 1000, "stock" : 10},
    {"nombre" : "cuaderno", "precio" : 5000, "stock" : 20},
    {"nombre" : "borrador", "precio" : 1000, "stock" : 35},
    {"nombre" : "regla", "precio" : 2000, "stock" : 45},
    {"nombre" : "tijera", "precio" : 7000, "stock" : 10},
    {"nombre" : "tinta", "precio" : 15000, "stock" : 24},
    {"nombre" : "papel", "precio" : 20000, "stock" : 30},
    {"nombre" : "pegamento", "precio" : 10000, "stock" : 50},
    {"nombre" : "sacapunta", "precio" : 1000, "stock" : 100},    

]

carrito = []

def mostrar_productos():
    print("---------------Menú de Productos----------------")
    for i, producto in enumerate(productos):
        print(f"{i+1}.{producto['nombre']} - precio ${producto['precio']} - cantidad {producto['stock']}")

def agregar_al_carrito():
    mostrar_productos()
    try:
        opcion=int(input("Digite el Producto que desea agregar"))
        if 1 <= opcion <= len(productos):
            cantidad = int(input("Digite la cantidad de productos a comprar: "))
            producto = productos[opcion - 1]
            if cantidad > producto["stock"]:
                print("No hay suficiente existencia del Producto")
            else:
                productos[opcion - 1]['stock'] -= cantidad
                carrito.append({"nombre":producto["nombre"],"precio":producto["precio"],"stock":cantidad})
                print(f"Felicidades!! añadiste {cantidad}{producto['nombre']} de manera exitosa")
    except Exception as e:
        print("Se ha Producido un Errror", e)

mostrar_productos()