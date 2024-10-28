"""Aplicación de cine
vamos a tener una tabla donde tendremos nuestras peliculas - id, nombre, descripción, géneros, clasificación."""
peliculas = [
    {"nombre" : "Interestellar",
    "director" : "Christopher Nolan",
    "descripcion" : "Inspirada en la teoría del experto en relatividad Kip Stepehen Thorne sobre la existencia de los agujeros de gusano, y su función como canal para llevar a cabo los viajes en el tiempo. La historia gira en torno a un grupo de intrépidos exploradores que se adentran por uno de esos agujeros y viajan a través del mismo, encontrándose en otra dimensión. Un mundo desconocido se abre ante ellos y deberán luchar por mantenerse unidos si quieren volver de una pieza" , 
    "genero" : ["Ciencia ficción","Apocalíptica" , "Drama" , "Distopía" , "Épica"] ,
    "clasificacion" : "Exclusiva para mayores de 13 años",
    "duracion" : "169 Minutos",
    "Actores" : ["Matthew McConaughey" , "Anne Hathaway" , "Jessica Chastain" , "Bill Irwin" , "Mackenzie Foy" , "John Lithgow" , "Ellen Burstyn" , "Michael Caine" , "Matt Damon"]
    }
]
for indice, pelicula in enumerate(peliculas):
    print("pelicula entrontrada")

def mostrar_todas_las_peliculas(peliculas):
    print("--------Lista de Peliculas----------")
    for pelicula in peliculas:
        print(f"Nombre: {pelicula['nombre']}")
        print(f"Director: {pelicula['director']}")
        print(f"Descripción: {pelicula['descripcion']}")
        print(f"Género: {', '.join(pelicula['genero'])}")
        print(f"Clasificación: {pelicula['clasificacion']}")
        print(f"Duración: {pelicula['duracion']}")
        print(f"Actores: {', '.join(pelicula['Actores'])}")
        print("------------------------------------")



def actualizar_una_pelicula(id_actualizar,pelicula):
    for indice, pelicula in enumerate(peliculas):
        if id_actualizar == indice:
            print("Pelicula encontrada")
            # Solicitar la actualización de los campos
            nombre = input(f"Ingrese nuevo nombre de la película ({pelicula['nombre']}): ")
            director = input(f"Ingrese nuevo director de la película ({pelicula['director']}): ")
            descripcion = input(f"Ingrese nueva descripción de la película ({pelicula['descripcion']}): ")
            genero = input(f"Ingrese los nuevos géneros separados por comas ({', '.join(pelicula['genero'])}): ").split(',')
            clasificacion = input(f"Ingrese nueva clasificación ({pelicula['clasificacion']}): ")
            duracion = input(f"Ingrese nueva duración ({pelicula['duracion']}): ")
            actores = input(f"Ingrese los nuevos actores separados por comas ({', '.join(pelicula['Actores'])}): ").split(',')

            # Actualizar los valores en el diccionario
            pelicula['nombre'] = nombre if nombre else pelicula['nombre']
            pelicula['director'] = director if director else pelicula['director']
            pelicula['descripcion'] = descripcion if descripcion else pelicula['descripcion']
            pelicula['genero'] = [g.strip() for g in genero] if genero else pelicula['genero']
            pelicula['clasificacion'] = clasificacion if clasificacion else pelicula['clasificacion']
            pelicula['duracion'] = duracion if duracion else pelicula['duracion']
            pelicula['Actores'] = [a.strip() for a in actores] if actores else pelicula['Actores']

            print("Película actualizada exitosamente.")
            break
    else:
        print("Película no encontrada.")


def crear_pelicula(peliculas):
    print("----- Crear una nueva película -----")
    
    # Solicitar la información de la nueva película
    nombre = input("Ingrese el nombre de la película: ")
    director = input("Ingrese el nombre del director: ")
    descripcion = input("Ingrese la descripción de la película: ")
    genero = input("Ingrese los géneros separados por comas: ").split(',')
    clasificacion = input("Ingrese la clasificación: ")
    duracion = input("Ingrese la duración (en minutos): ")
    actores = input("Ingrese los actores separados por comas: ").split(',')
    
    # Crear un diccionario para la nueva película
    nueva_pelicula = {
        "nombre": nombre,
        "director": director,
        "descripcion": descripcion,
        "genero": [g.strip() for g in genero],  # Limpiar espacios en blanco
        "clasificacion": clasificacion,
        "duracion": f"{duracion} Minutos",
        "Actores": [a.strip() for a in actores]
    }
    
    # Agregar la nueva película a la lista
    peliculas.append(nueva_pelicula)
    print("Película creada exitosamente.")

def eliminar_pelicula(id_eliminar, peliculas):
    if 0 <= id_eliminar < len(peliculas):  # Comprobar si el índice es válido
        pelicula_eliminada = peliculas.pop(id_eliminar)  # Eliminar la película por índice
        print(f"La película '{pelicula_eliminada['nombre']}' ha sido eliminada exitosamente.")
    else:
        print("El ID proporcionado no es válido. No se encontró la película.")

def mostrar_menu():
    while True:
        print("\n----- Menú de Películas -----")
        print("1. Mostrar todas las películas")
        print("2. Crear una nueva película")
        print("3. Actualizar una película")
        print("4. Eliminar una película")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_todas_las_peliculas(peliculas)
        elif opcion == "2":
            crear_pelicula(peliculas)
        elif opcion == "3":
            try:
                id_actualizar = int(input("Ingrese el ID de la película a actualizar: "))
                actualizar_una_pelicula(id_actualizar, peliculas)
            except ValueError:
                print("El ID debe ser un número.")
        elif opcion == "4":
            try:
                id_eliminar = int(input("Ingrese el ID de la película a eliminar: "))
                eliminar_pelicula(id_eliminar, peliculas)
            except ValueError:
                print("El ID debe ser un número.")
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción correcta.")