#Lista de productos e inventario disponible
import os

Productos=[
    {"nombre":"Anillo de Diamante","precio":10000,"cantidad":5},
    {"nombre":"Anillo de Cuarzo","precio":400,"cantidad":8},
    {"nombre":"Anillo de Plata","precio":1000,"cantidad":12},
    {"nombre":"Anillo de Oro","precio":6000,"cantidad":5}
    ]
carrito=[]

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls') #limpiar terminal en windows
    else:
        os.system('clear') #limpiar terminal en linux o mac

def mostrar_productos():
    limpiar_pantalla()
    print("---------------Menú de Productos----------------")
    for i, producto in enumerate(Productos):
        print(f"{i+1}.{producto['nombre']} - precio ${producto['precio']} - cantidad {producto['cantidad']}")


def agregar_al_carrito():
    limpiar_pantalla()
    mostrar_productos()
    try:
        opcion=int(input("Digite el Producto que desea agregar"))
        if 1 <= opcion <= len(Productos):
            cantidad = int(input("Digite la cantidad de productos a comprar: "))
            producto = Productos[opcion - 1]
            if cantidad > producto["cantidad"]:
                print("No hay suficiente existencia del Producto")
            else:
                Productos[opcion - 1]['cantidad'] -= cantidad
                carrito.append({"nombre":producto["nombre"],"precio":producto["precio"],"cantidad":cantidad})
                print(f"Felicidades!! añadiste {cantidad}{producto["nombre"]} de manera exitosa")


    except Exception as e:
        print("Se ha Producido un Errror", e)

def mostrar_carrito():
    limpiar_pantalla
    if carrito:
        print("carrito de compras")
        for i, item in enumerate(carrito, 1):
            print(f"{i}.producto: {item["nombre"]} - ${item["precio"]} - cantidad: {item["cantidad"]}")
    else:
        print("El carrito está vacio")

def calcular_total():
    total = sum(item["precio"]* item["cantidad"] for item in carrito)
    print(f"El Total a pagar es: ${total}")


def finalizar_compra():
    limpiar_pantalla()
    mostrar_carrito()

    if carrito:
        calcular_total()
        confirmar = input("¿Desea finalizar su compra? (s/n)?")

        if confirmar.lower()== "s":
            carrito.clear()
            print("La compra fue realizada exitosamente")
        else:
            print("La compra fue cancelada")
    else:
        print("No hay productos en el carrito")

def main():
    while True:
        limpiar_pantalla()
        print("----------MENÚ JOYERÍA----------")
        print("1- Mostrar productos disponibles")
        print("2- Añadir Productos al carrito")
        print("3- mostrar carrito")
        print("4- Finalizar compra")
        print("5- Salir de la compra")

        try:
            opciones={
                1: mostrar_productos,
                2: agregar_al_carrito,
                3: mostrar_carrito,
                4: finalizar_compra
            }

            seleccion=int(input("Digite la opción deseada "))
            if seleccion in opciones:
                opciones[seleccion]()
                input("Precione enter para continuar")
            elif seleccion == 5:
                break
        except ValueError:
            print("La entrada no es valida, por favor digite un número")
            input("precione enter para continuar...")
        except Exception:
            print("Se ha producido un Error")
            input("precione enter para continuar...")

main()