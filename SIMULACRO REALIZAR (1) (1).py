# â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
#  EVALUACIÃ“N PRÃCTICA â€” ProgramaciÃ³n de computadores
#  Sistema de GestiÃ³n: PixelZone Gaming ðŸŽ®

# â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
#
#  INSTRUCCIONES:
#  - Complete ÃšNICAMENTE las 4 funciones indicadas.
#  - NO modifique la funciÃ³n main() ni los datos precargados.
#  - Cada funciÃ³n tiene su firma y DocString que describe exactamente
#    lo que debe hacer, quÃ© recibe y quÃ© retorna o imprime.
#  - Maneje excepciones donde se indique (ValueError, KeyError).
#
# â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•


# â”€â”€ FUNCIÃ“N 1 â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

def mostrar_informacion(inventario):
    juegos = input("Ingrese el nombre del juego: ").strip()
    if  not juegos in inventario:
        print(f"ERROR: El video juego '{juegos}' no fue encontrado")
    else :
        juego = inventario[juegos]
        nombre = juego["nombre"]
        categoria = juego["categoria"]
        precio = juego ["precio"]
        stock = juego ["stock"]
        
        print(f"Nombre: {nombre}")
        print(f"Categoria: {categoria}")
        print(f"Precio: {precio:,.2f}")
        print(f"Stock: {stock}")
        if stock > 0:
            print("Estado disponible")
        elif stock == 0:
            print("Estado agotado")
    """
    Solicita al usuario la clave de un videojuego y muestra sus
    datos bÃ¡sicos: nombre, categorÃ­a, precio y stock.

    ParÃ¡metros:
        inventario (dict): Diccionario principal con todos los videojuegos.

    Comportamiento esperado:
        1. Pedir al usuario la clave del videojuego (str).
        2. Verificar si la clave existe en el inventario usando 'in'.
           - Si NO existe: imprimir "Error: El videojuego '<clave>' no
             fue encontrado."
           - Si SÃ existe:
             a) Imprimir el nombre (str).
             b) Imprimir la categorÃ­a (str).
             c) Imprimir el precio (float) con 2 decimales.
             d) Imprimir el stock (int).
             e) Si el stock es mayor a 0, imprimir "Estado: Disponible".
                Si el stock es 0, imprimir "Estado: Agotado".

    Retorna:
        None (solo imprime en consola).
    """
    pass


# â”€â”€ FUNCIÃ“N 2 â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
def agregar_puntaje(inventario):
    juegos = input("Ingresa la clave del videojuego: ").strip()

   
    if juegos not in inventario:
        print(f"Error: El videojuego '{juegos}' no fue encontrado.")
        return

    try:
       
        valor = float(input("Ingrese el puntaje (0.0 a 5.0): "))

       
        if valor < 0.0 or valor > 5.0:
            print("Error: El puntaje debe estar entre 0.0 y 5.0")
            return

       
        inventario[juegos]["puntajes"].append(valor)

       
        print("Puntaje registrado exitosamente.")
        print(f"Total de puntajes: {len(inventario[juegos]['puntajes'])}")

    except ValueError:
        print("Error: Debe ingresar un valor numérico.")
    
    """
    Permite agregar un nuevo puntaje a la lista de puntajes de un
    videojuego existente en el inventario.

    ParÃ¡metros:
        inventario (dict): Diccionario principal con todos los videojuegos.

    Comportamiento esperado:
        1. Pedir al usuario la clave del videojuego (str).
        2. Verificar si la clave existe en el inventario usando 'in'.
           - Si NO existe: imprimir "Error: El videojuego '<clave>' no
             fue encontrado."
        3. Si existe, pedir al usuario el puntaje como un nÃºmero decimal.
           - Convertir el valor ingresado a float.
        4. Validar que el puntaje estÃ© entre 0.0 y 5.0 (inclusive).
           - Si estÃ¡ fuera del rango: imprimir
             "Error: El puntaje debe estar entre 0.0 y 5.0"
        5. Agregar el puntaje al final de la lista usando append().
        6. Imprimir "Puntaje registrado exitosamente."
        7. Imprimir la cantidad total de puntajes que ahora tiene
           el juego usando len().

    Retorna:
        None (solo imprime en consola).

    Excepciones a manejar:
        - ValueError: si el usuario ingresa un texto que no se puede
          convertir a float (ejemplo: "abc"). En ese caso imprimir
          "Error: Debe ingresar un valor numÃ©rico."
    """
    pass


# â”€â”€ FUNCIÃ“N 3 â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
def mostrar_detalle(inventario):
    juegos = input("Ingrese el nombre del juego: ").strip()
    if  not juegos in inventario:
        print(f"ERROR: El video juego '{juegos}' no fue encontrado")
    else :
        juego= inventario[juegos]
        mi_tuple= juego["clasificacion"]
        print(f"----- Clasificacion -----")
        print(f"Codigo: {mi_tuple[0]}")
        print(f"Descripcion: {mi_tuple[1]}")
        print(f"Edad minima: {mi_tuple[2]}")
        plataformas = juego["plataformas"]
        print(f"----- Plataformas -----")
    for plataforma in plataformas:
        print(f"- {plataforma}")
    print(f"Total: {len(plataformas)} plataformas")
    desarrollador= juego["desarrollador"]
    nombre= desarrollador["nombre"]
    pais= desarrollador["pais"]
    fundado= desarrollador ["fundado"]
    print(f"----- Desarrollador -----")
    print(f"Nombre: {nombre}")
    print(f"Pais: {pais}")
    print(f"Fundado: {fundado}")
    
        

    """
    Solicita al usuario la clave de un videojuego y muestra la
    informaciÃ³n que estÃ¡ almacenada en la tupla, el conjunto y el
    diccionario anidado de ese juego.

    ParÃ¡metros:
        inventario (dict): Diccionario principal con todos los videojuegos.

    Comportamiento esperado:
        1. Pedir al usuario la clave del videojuego (str).
        2. Verificar si la clave existe en el inventario usando 'in'.
           - Si NO existe: imprimir "Error: El videojuego '<clave>' no
             fue encontrado."
           - Si SÃ existe:

             a) TUPLA â€” ClasificaciÃ³n:
                Imprimir el cÃ³digo accediendo al Ã­ndice 0 de la tupla.
                Imprimir la descripciÃ³n accediendo al Ã­ndice 1.
                Imprimir la edad mÃ­nima accediendo al Ã­ndice 2.

             b) CONJUNTO â€” Plataformas:
                Recorrer el conjunto con un for e imprimir cada
                plataforma.
                Imprimir la cantidad total de plataformas usando len().

             c) DICCIONARIO ANIDADO â€” Desarrollador:
                Imprimir el nombre accediendo con la clave "nombre".
                Imprimir el paÃ­s accediendo con la clave "pais".
                Imprimir el aÃ±o de fundaciÃ³n con la clave "fundado".

    Retorna:
        None (solo imprime en consola).
    """
    pass


# â”€â”€ FUNCIÃ“N 4 â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
def resumen_inventario(inventario):
    if len(inventario)==0:
        print("El inventario esta vacio")
        return False
    total_juegos= len(inventario)
    disponibles= 0
    agotados= 0
    precio= 0
    for juego in inventario.values():
        if juego["stock"] > 0:
            disponibles += 1
        else:
            agotados += 1
        precio += juego["precio"]
    promedio_precio= precio/total_juegos
    print(f"Numero de juegos: {total_juegos}")
    print(f"Juegos disponibles: {disponibles}")
    print(f"Juegos agotados: {agotados}")
    print(f"Precio promedio: {promedio_precio}")            
    """
    Recorre todo el diccionario principal y muestra un resumen
    general del inventario.

    ParÃ¡metros:
        inventario (dict): Diccionario principal con todos los videojuegos.

    Comportamiento esperado:
        1. Si el inventario estÃ¡ vacÃ­o (len == 0), imprimir
           "El inventario estÃ¡ vacÃ­o." y terminar la funciÃ³n con return.

        2. Recorrer todos los videojuegos del diccionario y calcular:

           a) El total de videojuegos (int) â€” usar len() sobre el
              diccionario.

           b) CuÃ¡ntos estÃ¡n disponibles (stock > 0) y cuÃ¡ntos estÃ¡n
              agotados (stock == 0) â€” usar un for con un contador
              para cada caso.

           c) El precio promedio (float) de todos los juegos â€” sumar
              todos los precios y dividir entre el total. Mostrar con
              2 decimales.

        3. Imprimir los tres resultados anteriores de forma clara.

    Retorna:
        None (solo imprime en consola).
    """
    pass


# â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
#  FUNCIÃ“N MAIN â€” Â¡NO MODIFICAR!
# â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
def main():
    """
    FunciÃ³n principal del sistema de gestiÃ³n de la tienda de videojuegos.
    Contiene los datos precargados y el menÃº interactivo de la aplicaciÃ³n.

    *** ESTA FUNCIÃ“N ESTÃ COMPLETA. NO DEBE SER MODIFICADA. ***
    """

    # â”€â”€ DICCIONARIO PRINCIPAL: Inventario de videojuegos â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    # Cada videojuego contiene internamente las siguientes estructuras:
    #   str   â†’ "nombre", "categoria"
    #   float â†’ "precio"
    #   int   â†’ "stock"
    #   tuple â†’ "clasificacion" (cÃ³digo, descripciÃ³n, edad mÃ­nima)
    #   list  â†’ "puntajes" (calificaciones float de 0.0 a 5.0)
    #   set   â†’ "plataformas" (sin duplicados)
    #   dict  â†’ "desarrollador" (nombre, paÃ­s, aÃ±o de fundaciÃ³n)

    inventario_juegos = {
        "the legend of zelda": {
            "nombre"        : "The Legend of Zelda: Tears of the Kingdom",
            "categoria"     : "Aventura",
            "precio"        : 249990.50,
            "stock"         : 25,
            "clasificacion" : ("E10+", "Everyone 10+", 10),
            "puntajes"      : [4.9, 5.0, 4.8, 4.7, 5.0],
            "plataformas"   : {"nintendo switch"},
            "desarrollador" : {
                "nombre" : "Nintendo EPD",
                "pais"   : "JapÃ³n",
                "fundado": 1889
            }
        },
        "god of war ragnarok": {
            "nombre"        : "God of War: RagnarÃ¶k",
            "categoria"     : "AcciÃ³n",
            "precio"        : 279990.75,
            "stock"         : 18,
            "clasificacion" : ("M", "Mature", 17),
            "puntajes"      : [5.0, 4.8, 4.9, 4.6, 4.8],
            "plataformas"   : {"ps4", "ps5", "pc"},
            "desarrollador" : {
                "nombre" : "Santa Monica Studio",
                "pais"   : "Estados Unidos",
                "fundado": 1999
            }
        },
        "minecraft": {
            "nombre"        : "Minecraft",
            "categoria"     : "Sandbox",
            "precio"        : 119990.00,
            "stock"         : 50,
            "clasificacion" : ("E10+", "Everyone 10+", 10),
            "puntajes"      : [4.5, 4.7, 4.3, 4.8, 4.6],
            "plataformas"   : {"pc", "ps4", "ps5", "xbox one", "xbox series x", "nintendo switch", "android", "ios"},
            "desarrollador" : {
                "nombre" : "Mojang Studios",
                "pais"   : "Suecia",
                "fundado": 2009
            }
        },
        "elden ring": {
            "nombre"        : "Elden Ring",
            "categoria"     : "RPG",
            "precio"        : 239990.25,
            "stock"         : 12,
            "clasificacion" : ("M", "Mature", 17),
            "puntajes"      : [4.8, 5.0, 4.6, 4.9, 4.7],
            "plataformas"   : {"pc", "ps4", "ps5", "xbox one", "xbox series x"},
            "desarrollador" : {
                "nombre" : "FromSoftware",
                "pais"   : "JapÃ³n",
                "fundado": 1986
            }
        },
        "Fifa 25": {
            "nombre"        : "EA Sports FC 25",
            "categoria"     : "Deportes",
            "precio"        : 199990.99,
            "stock"         : 30,
            "clasificacion" : ("E", "Everyone", 6),
            "puntajes"      : [3.5, 3.8, 3.2, 4.0, 3.6],
            "plataformas"   : {"pc", "ps5", "xbox series x", "nintendo switch"},
            "desarrollador" : {
                "nombre" : "EA Vancouver",
                "pais"   : "CanadÃ¡",
                "fundado": 1983
            }
        },
        "resident evil 4": {
            "nombre"        : "Resident Evil 4 Remake",
            "categoria"     : "Terror",
            "precio"        : 229990.50,
            "stock"         : 0,
            "clasificacion" : ("M", "Mature", 17),
            "puntajes"      : [4.7, 4.9, 4.5, 4.8, 4.6],
            "plataformas"   : {"pc", "ps4", "ps5", "xbox series x"},
            "desarrollador" : {
                "nombre" : "Capcom",
                "pais"   : "JapÃ³n",
                "fundado": 1979
            }
        },
        "stardew valley": {
            "nombre"        : "Stardew Valley",
            "categoria"     : "SimulaciÃ³n",
            "precio"        : 59990.00,
            "stock"         : 40,
            "clasificacion" : ("E10+", "Everyone 10+", 10),
            "puntajes"      : [4.6, 4.8, 4.9, 4.5, 4.7],
            "plataformas"   : {"pc", "ps4", "xbox one", "nintendo switch", "android", "ios"},
            "desarrollador" : {
                "nombre" : "ConcernedApe",
                "pais"   : "Estados Unidos",
                "fundado": 2016
            }
        },
        "call of duty modern warfare 3": {
            "nombre"        : "Call of Duty: Modern Warfare III",
            "categoria"     : "Shooter",
            "precio"        : 269990.75,
            "stock"         : 22,
            "clasificacion" : ("M", "Mature", 17),
            "puntajes"      : [3.2, 3.5, 3.0, 3.8, 3.4],
            "plataformas"   : {"pc", "ps4", "ps5", "xbox one", "xbox series x"},
            "desarrollador" : {
                "nombre" : "Sledgehammer Games",
                "pais"   : "Estados Unidos",
                "fundado": 2009
            }
        },
        "hollow_knight": {
            "nombre"        : "Hollow Knight",
            "categoria"     : "Metroidvania",
            "precio"        : 49990.25,
            "stock"         : 0,
            "clasificacion" : ("E10+", "Everyone 10+", 10),
            "puntajes"      : [4.9, 5.0, 4.8, 4.9, 5.0],
            "plataformas"   : {"pc", "ps4", "xbox one", "nintendo switch"},
            "desarrollador" : {
                "nombre" : "Team Cherry",
                "pais"   : "Australia",
                "fundado": 2014
            }
        },
        "mario kart 8": {
            "nombre"        : "Mario Kart 8 Deluxe",
            "categoria"     : "Carreras",
            "precio"        : 219990.00,
            "stock"         : 15,
            "clasificacion" : ("E", "Everyone", 6),
            "puntajes"      : [4.7, 4.5, 4.8, 4.6, 4.9],
            "plataformas"   : {"nintendo switch"},
            "desarrollador" : {
                "nombre" : "Nintendo EPD",
                "pais"   : "JapÃ³n",
                "fundado": 1889
            }
        }
    }

    # â”€â”€ MENÃš PRINCIPAL â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
    while True:
        print()
        print("â•”â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•—")
        print("â•‘   ðŸŽ®  SISTEMA DE GESTIÃ“N â€” PIXELZONE GAMING  ðŸŽ®  â•‘")
        print("â• â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•£")
        print("â•‘  1. Mostrar informaciÃ³n de un videojuego         â•‘")
        print("â•‘  2. Agregar puntaje a un videojuego              â•‘")
        print("â•‘  3. Mostrar detalle completo de un videojuego    â•‘")
        print("â•‘  4. Resumen general del inventario               â•‘")
        print("â•‘  5. Salir del sistema                            â•‘")
        print("â•šâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•")

        opcion = input("  Seleccione una opciÃ³n: ")

        match opcion:
            case "1":
                mostrar_informacion(inventario_juegos)
            case "2":
                agregar_puntaje(inventario_juegos)
            case "3":
                mostrar_detalle(inventario_juegos)
            case "4":
                resumen_inventario(inventario_juegos)
            case "5":
                print("\n  Â¡Gracias por usar PixelZone Gaming! ðŸ‘¾\n")
                break
            case _:
                print("\n  âš ï¸  OpciÃ³n no vÃ¡lida. Intente de nuevo.")


# â”€â”€ Punto de entrada â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
if __name__ == "__main__":
    main()