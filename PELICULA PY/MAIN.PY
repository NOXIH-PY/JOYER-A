directores = [{
    "nombre":"Christopher Nolan",
    "edad": 51,
    "genero":"Masculino",
},

{
    "nombre":"Quentin Tarantino",
    "edad": 62,
    "genero":"Masculino",
},

{
    "nombre":"Martin Scorsese",
    "edad": 71,
    "genero":"Masculino",
},
]

peliculas = [
    {
        "nombre":"Interstellar",
        "director":"Christopher Nolan",
        "genero":"Ciencia ficcion",
        "clasificacion":"Exclusiva para mayores de 13 años",
        "duracion":"169 Minutos"},

    {
        "nombre":"Avatar",
        "director":"James Cameron",
        "genero":"Ciencia ficcion",
        "clasificacion":"Exclusiva para mayores de 13 años",
        "duracion":"162 Minutos"},

    {
        "nombre":"El Juego de Ender",
        "director":"Gavin Hood",
        "genero":"Acción",
        "clasificacion":"Exclusiva para mayores de 13 años",
        "duracion":"1h 54min"},
]
def mostrar_peliculas():
    for pelicula in peliculas:
        print(f"Nombre: {pelicula['nombre']}")
        print(f"Director: {pelicula['director']}")
        print(f"Genero: {pelicula['genero']}")
        print(f"Clasificacion: {pelicula['clasificacion']}")
        print(f"Duracion: {pelicula['duracion']}")
        print()

mostrar_peliculas(peliculas)