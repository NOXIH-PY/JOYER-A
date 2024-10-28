usuario = {
    "usuario" : {"contrasena": "1234" , "saldo" : 10000},
    "usuario2" : {"contrasena": "5678" , "saldo" : 80000},
    "usuario3" : {"contrasena": "9101" , "saldo" : 100},
    "usuario4" : {"contrasena": "1254" , "saldo" : 5000},
    "usuario5" : {"contrasena": "1250" , "saldo" : 15000}
    }

def autentificarusuario(nombre,contrasena):
    usuario = usuario.get(nombre)
    if usuario and usuario.get("contrasena") == contrasena:
        return True
    return False

def consultarsaldo(usuario):
    return usuario.get("saldo")

def reretirar_dinero(usuario,cantidad):
    if cantidad > 0:
        if cantidad <= usuario.get("saldo"):
            usuario["saldo"] -= cantidad
            return f"Se han retirado ${cantidad} de tu cuenta"
        return "No hay suficiente dinero en tu cuenta"
    
def depositar_dinero(usuario,cantidad):
    if cantidad > 0:
        usuario["saldo"] += cantidad
        return f"Se han depositado ${cantidad} a tu cuenta"
    return "La cantidad debe ser mayor a 0"

#cambiar contrasena verificando la contrasena anterior
def cambiarcontrasena():
    contrasenaactual = input("Ingresa tu contrasena actual: ")
    if contrasenaactual == usuario.get("contrasena"):
        nuevacontrasena = input("Ingresa tu nueva contrasena: ")
        usuario["contrasena"] = nuevacontrasena
        return f"tu contrasena actual se a cambiado con exito"
    return f"tu contrasena actual no coincide"


#creación de menu que va ha permitir autentificar si el usuario esta creado y luego de autentificarlo me va ha permitir revisar las opciones del cajero

def menu():
    while True:
        nombre = input("Ingresa tu nombre: (exit para salir)")
        if nombre.lower() == "exit":
            break
        contrasena = input("Ingresa tu contrasena: ")
        autentificado = autentificarusuario(nombre,contrasena)
        if not autentificado:
            print("El usuario no existe o la contrasena es incorrecta")
            continue
        print(f"Bienvenido {nombre}")
        while True:
            print("----------Menú----------")
            print("1. Consultar saldo")
            print("2. Retirar dinero")
            print("3. Depositar dinero")
            print("4. Salir")
            print("------------------------")
            try:
                opcion = int(input("Ingresa una de las opciones: "))
                if opcion == 1:
                    print(f"Tu saldo actual es de ${consultarsaldo(usuario[nombre])}")
                elif opcion == 2:
                    cantidad = float(input("Ingresa la cantidad que deseas retirar: "))
                elif opcion == 3:
                    cantidad = int(input("Ingresa la cantidad que deseas depositar: "))
                elif opcion == 4:
                    cambiarcontrasena()
                elif opcion == 5:
                    break # Salir del bucle while y terminar el programa("Hasta Pronto")
                else:
                    print("La opcion no existe")


            except ValueError:
                print("La entrada no es valida, por favor digite un número")


menu()