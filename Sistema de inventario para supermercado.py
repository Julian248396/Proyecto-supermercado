info_tienda = (
    "La Bodega",
    "Vallecito, Tolima",
    "Tienda Local",
    2020
)



def mostrar_inventario(inventario_tienda):
    
    if not inventario_tienda:
        print("\n  El inventario está vacío.")
        return

    print("\n" + "=" * 52)
    print("INVENTARIO COMPLETO".center(52))
    print("=" * 52)

    for clave, producto in inventario_tienda.items():
        estado = "Disponible" if producto["cantidad"] > 0 else "Agotado"
        print(f"\n  Clave     : {clave}")
        print(f"  Nombre    : {producto['nombre']}")
        print(f"  Categoría : {producto['categoria']}")
        print(f"  Precio    : ${producto['precio']:,.0f}")
        print(f"  Cantidad  : {producto['cantidad']}")
        print(f"  Estado    : {estado}")
        print("  " + "-" * 48)



def mostrar_detalle_producto(inventario_tienda):
  
    clave = input("\n  Ingrese la clave del producto: ").strip().lower()

    if clave not in inventario_tienda:
        print(f"\n  Error: El producto '{clave}' no fue encontrado.")
        return

    p = inventario_tienda[clave]

    print("\n" + "=" * 52)
    print("DETALLE DEL PRODUCTO".center(52))
    print("=" * 52)


    print(f"\n  Nombre    : {p['nombre']}")
    print(f"  Categoría : {p['categoria']}")
    print(f"  Precio    : ${p['precio']:,.0f}")
    print(f"  Cantidad  : {p['cantidad']}")


    unidad = p["unidad_medida"]
    print(f"\n  --- Unidad de Medida ---")
    print(f"  Tipo        : {unidad[0]}")
    print(f"  Abreviatura : {unidad[1]}")
    print(f"  Referencia  : {unidad[2]} {unidad[1]}")


    print(f"\n  --- Etiquetas ---")
    for etiqueta in p["etiquetas"]:
        print(f"  - {etiqueta}")


    promedio = calcular_promedio_precios(p["historial_precios"])
    print(f"\n  --- Historial de Precios ---")
    print(f"  Precios registrados : {p['historial_precios']}")
    print(f"  Precio promedio     : ${promedio:,.0f}")


    prov = p["proveedor"]
    print(f"\n  --- Proveedor ---")
    print(f"  Nombre    : {prov['nombre']}")
    print(f"  Ciudad    : {prov['ciudad']}")
    print(f"  Teléfono  : {prov['telefono']}")




def analisis_inventario(inventario_tienda):

    while True:
        mostrar_menu("ANÁLISIS DEL INVENTARIO", [
            "Ver categorías únicas",
            "Ver productos agotados",
            "Ver producto más caro y más barato",
            "Volver"
        ])

        opcion = input("  Seleccione: ")

        match opcion:
            case "1":
                categorias = set()

                for p in inventario_tienda.values():
                    categorias.add(p["categoria"])

                print(f"\n  Categorías únicas ({len(categorias)}): {categorias}")

            case "2":
                agotados = []

                for p in inventario_tienda.values():
                    if p["cantidad"] == 0:
                        agotados.append(p["nombre"])

                if agotados:
                    print("\n  Productos agotados:")
                    for nombre in agotados:
                        print(f"  - {nombre}")
                else:
                    print("\n  No hay productos agotados.")

            case "3":
                if not inventario_tienda:
                    print("\n  El inventario está vacío.")
                    continue
                mas_caro = max(inventario_tienda.values(), key=lambda p: p["precio"])
                mas_barato = min(inventario_tienda.values(), key=lambda p: p["precio"])
                print(f"\n  Más caro  : {mas_caro['nombre']} - ${mas_caro['precio']:,.0f}")
                print(f"  Más barato: {mas_barato['nombre']} - ${mas_barato['precio']:,.0f}")

            case "4":
                break

            case _:
                print("  Opción inválida.")




def informacion_tienda(inventario_tienda):
  """
    Muestra los datos generales de La Bodeguita almacenados en la tupla info_tienda.

    Opción 1: Imprime todos los datos de la tienda (nombre, dirección, tipo, año).
    Opción 2: Permite al usuario consultar un dato específico ingresando su índice.
              Maneja errores de tipo ValueError e IndexError si el índice es inválido.

    Parámetros:
        inventario_tienda (dict): Recibido por consistencia con los demás módulos,
                                  aunque esta función usa la tupla global info_tienda.

    Retorna:
        None (solo imprime en consola).
    """
    while True:
        mostrar_menu("INFORMACIÓN DE LA TIENDA", [
            "Ver información completa",
            "Volver"
        ])

        opcion = input("  Seleccione: ")

        match opcion:
            case "1":
                print(f"\n  Nombre   : {info_tienda[0]}")
                print(f"  Dirección: {info_tienda[1]}")
                print(f"  Tipo     : {info_tienda[2]}")
                print(f"  Año      : {info_tienda[3]}")

            case "2":
                break

            case _:
                print("  Opción inválida.")



def gestionar_productos(inventario_tienda):
 """
    CRUD completo para administrar los productos del inventario.

    Opción 1 (Create):  Solicita todos los datos del nuevo producto y lo agrega
                        al diccionario con su estructura completa (str, float, int,
                        tuple, list, set y dict anidado del proveedor).
    Opción 2 (Read):    Consulta y muestra la información básica de un producto
                        por su clave, incluyendo datos del proveedor.
    Opción 3 (Update):  Permite modificar nombre, categoría, precio o cantidad.
                        Al cambiar el precio, guarda el valor anterior en historial_precios.
    Opción 4 (Delete):  Elimina un producto previa confirmación del usuario.
                        Los productos esenciales (arroz diana, leche entera) están protegidos.

    Parámetros:
        inventario_tienda (dict): Diccionario principal con todos los productos.

    Retorna:
        None (modifica el diccionario directamente en memoria).
    """
    while True:
        mostrar_menu("GESTIÓN DE PRODUCTOS", [
            "Agregar producto",
            "Consultar producto",
            "Modificar campo de un producto",
            "Eliminar producto",
            "Volver"
        ])

        opcion = input("  Seleccione: ")

        match opcion:


            case "1":
                print("\n  --- AGREGAR PRODUCTO ---")
                clave = input("  Clave única (ej: 'sal marina'): ").strip().lower()

                if clave in inventario_tienda:
                    print("  Ya existe un producto con esa clave.")
                    continue

                nombre = input("  Nombre del producto: ")
                categoria = input("  Categoría: ")

                try:
                    precio = float(input("  Precio: "))
                    cantidad = int(input("  Cantidad: "))
                except ValueError:
                    print("  Error: precio y cantidad deben ser números.")
                    continue

                tipo_unidad = input("  Tipo de unidad (ej: gramos): ")
                abrev_unidad = input("  Abreviatura (ej: g): ")

                try:
                    ref_unidad = int(input("  Referencia (ej: 500): "))
                except ValueError:
                    print("  Error: la referencia debe ser un número entero.")
                    continue

                nom_proveedor = input("  Nombre del proveedor: ")
                ciudad_proveedor = input("  Ciudad del proveedor: ")
                tel_proveedor = input("  Teléfono del proveedor: ")

                inventario_tienda[clave] = {
                    "nombre": nombre,
                    "categoria": categoria,
                    "precio": precio,
                    "cantidad": cantidad,
                    "unidad_medida": (tipo_unidad, abrev_unidad, ref_unidad),
                    "historial_precios": [precio],
                    "etiquetas": set(),
                    "proveedor": {
                        "nombre": nom_proveedor,
                        "ciudad": ciudad_proveedor,
                        "telefono": tel_proveedor
                    }
                }
                print(f"\n  Producto '{nombre}' agregado correctamente.")

 
            case "2":
                clave = input("\n  Clave del producto a consultar: ").strip().lower()
                if clave in inventario_tienda:
                    p = inventario_tienda[clave]
                    print(f"\n  Nombre    : {p['nombre']}")
                    print(f"  Categoría : {p['categoria']}")
                    print(f"  Precio    : ${p['precio']:,.0f}")
                    print(f"  Cantidad  : {p['cantidad']}")
                    print(f"  Proveedor : {p['proveedor']['nombre']} ({p['proveedor']['ciudad']})")
                else:
                    print(f"\n  Error: '{clave}' no fue encontrado.")


            case "3":
                clave = input("\n  Clave del producto a modificar: ").strip().lower()
                if clave not in inventario_tienda:
                    print(f"\n  Error: '{clave}' no fue encontrado.")
                    continue

                p = inventario_tienda[clave]
                print("\n  Campos modificables:")
                print("  1. nombre")
                print("  2. categoria")
                print("  3. precio")
                print("  4. cantidad")

                campo_op = input("  Seleccione campo (1-4): ")

                match campo_op:
                    case "1":
                        p["nombre"] = input("  Nuevo nombre: ")
                        print("  Nombre actualizado.")
                    case "2":
                        p["categoria"] = input("  Nueva categoría: ")
                        print("  Categoría actualizada.")
                    case "3":
                        try:
                            nuevo_precio = float(input("  Nuevo precio: "))
                            p["historial_precios"].append(p["precio"])
                            p["precio"] = nuevo_precio
                            print("  Precio actualizado y guardado en historial.")
                        except ValueError:
                            print("  Error: ingrese un número válido.")
                    case "4":
                        try:
                            p["cantidad"] = int(input("  Nueva cantidad: "))
                            print("  Cantidad actualizada.")
                        except ValueError:
                            print("  Error: ingrese un número entero.")
                    case _:
                        print("  Opción inválida.")


            case "4":
                clave = input("\n  Clave del producto a eliminar: ").strip().lower()
                if clave not in inventario_tienda:
                    print(f"\n  Error: '{clave}' no fue encontrado.")
                    continue

                if clave in ["arroz diana", "leche entera"]:
                    print("  Este producto es esencial y no se puede eliminar.")
                    continue

                confirmacion = input(f"  ¿Eliminar '{clave}'? (s/n): ").lower()
                if confirmacion == "s":
                    del inventario_tienda[clave]
                    print("  Producto eliminado correctamente.")
                else:
                    print("  Eliminación cancelada.")

            case "5":
                break

            case _:
                print("  Opción inválida.")

                
def mostrar_menu(titulo, opciones):
 """
    Función auxiliar que imprime un menú formateado con título y opciones numeradas.

    Dibuja una línea de separación, centra el título y lista cada opción
    con su número correspondiente. Es reutilizada por todos los módulos del sistema.

    Parámetros:
        titulo  (str):  Texto que se muestra centrado como encabezado del menú.
        opciones (list): Lista de strings, cada uno representa una opción del menú.

    Retorna:
        None (solo imprime en consola).
    """
    print("\n" + "=" * 52)
    print(titulo.center(52))
    print("=" * 52)
    for i, op in enumerate(opciones, 1):
        print(f"  {i}. {op}")
    print("=" * 52)


def calcular_promedio_precios(historial):
 """
    Función auxiliar que calcula el precio promedio a partir de un historial de precios.

    Suma todos los valores de la lista y los divide entre la cantidad de elementos.
    Es usada por mostrar_detalle_producto() para mostrar el promedio al usuario.

    Parámetros:
        historial (list): Lista de precios flotantes registrados históricamente.

    Retorna:
        float: Promedio de los precios. Retorna 0 si la lista está vacía.
    """
    if not historial:
        return 0
    return sum(historial) / len(historial)




def main():
     """
    Función principal del sistema. Inicializa el inventario con los productos
    precargados y lanza el menú principal en un bucle hasta que el usuario
    elija salir.

    El inventario_tienda es un diccionario de diccionarios anidados donde cada
    clave es el nombre del producto en minúsculas y su valor contiene todas
    las estructuras de datos del producto (str, float, int, tuple, list, set, dict).

    Retorna:
        None.
    """
    inventario_tienda = {
    "arroz diana": {
        "nombre": "Arroz Diana x 500g",
        "categoria": "Granos",
        "precio": 3200.0,
        "cantidad": 80,
        "unidad_medida": ("gramos", "g", 500),
        "historial_precios": [2900.0, 3000.0, 3100.0, 3200.0],
        "etiquetas": {"sin gluten", "basico", "popular"},
        "proveedor": {
            "nombre": "Distribuidora El Granero",
            "ciudad": "Ibague",
            "telefono": "3001234567"
        }
    },
    "aceite vegetal": {
        "nombre": "Aceite Vegetal x 1L",
        "categoria": "Aceites",
        "precio": 8500.0,
        "cantidad": 45,
        "unidad_medida": ("litros", "L", 1),
        "historial_precios": [7800.0, 8000.0, 8300.0, 8500.0],
        "etiquetas": {"cocina", "basico"},
        "proveedor": {
            "nombre": "Comercial La Estrella",
            "ciudad": "Bogota",
            "telefono": "3109876543"
        }
    },
    "leche entera": {
        "nombre": "Leche Entera Alqueria x 1L",
        "categoria": "Lacteos",
        "precio": 4200.0,
        "cantidad": 60,
        "unidad_medida": ("litros", "L", 1),
        "historial_precios": [3800.0, 4000.0, 4100.0, 4200.0],
        "etiquetas": {"refrigerado", "popular", "lacteo"},
        "proveedor": {
            "nombre": "Alqueria S.A.",
            "ciudad": "Cajica",
            "telefono": "3154567890"
        }
    },
    "panela redonda": {
        "nombre": "Panela Redonda x 500g",
        "categoria": "Endulzantes",
        "precio": 2800.0,
        "cantidad": 100,
        "unidad_medida": ("gramos", "g", 500),
        "historial_precios": [2400.0, 2500.0, 2700.0, 2800.0],
        "etiquetas": {"natural", "popular", "tolimense"},
        "proveedor": {
            "nombre": "Trapiche Don Pedro",
            "ciudad": "Honda",
            "telefono": "3178901234"
        }
    },
    "jabon rey": {
        "nombre": "Jabon Rey x 3 unidades",
        "categoria": "Aseo",
        "precio": 5500.0,
        "cantidad": 35,
        "unidad_medida": ("unidades", "und", 3),
        "historial_precios": [4900.0, 5100.0, 5300.0, 5500.0],
        "etiquetas": {"aseo", "hogar"},
        "proveedor": {
            "nombre": "Unilever Colombia",
            "ciudad": "Medellin",
            "telefono": "3123456789"
        }
    },
    "atun van camps": {
        "nombre": "Atun Van Camps x 170g",
        "categoria": "Enlatados",
        "precio": 4800.0,
        "cantidad": 0,
        "unidad_medida": ("gramos", "g", 170),
        "historial_precios": [4200.0, 4400.0, 4600.0, 4800.0],
        "etiquetas": {"proteina", "enlatado"},
        "proveedor": {
            "nombre": "Van Camps Colombia",
            "ciudad": "Barranquilla",
            "telefono": "3201234567"
        }
    },
    "pasta el dorado": {
        "nombre": "Pasta El Dorado x 500g",
        "categoria": "Pastas",
        "precio": 3500.0,
        "cantidad": 55,
        "unidad_medida": ("gramos", "g", 500),
        "historial_precios": [3000.0, 3200.0, 3400.0, 3500.0],
        "etiquetas": {"basico", "popular"},
        "proveedor": {
            "nombre": "Molinos El Dorado",
            "ciudad": "Cali",
            "telefono": "3165432109"
        }
    }
}

    while True:
        mostrar_menu("SISTEMA DE INVENTARIO - LA BODEGA", [
            "Gestión de productos",
            "Ver inventario completo",
            "Ver detalle de un producto",
            "Análisis del inventario",
            "Información de la tienda",
            "Salir"
        ])

        opcion = input("  Seleccione: ")

        match opcion:
            case "1":
                gestionar_productos(inventario_tienda)
            case "2":
                mostrar_inventario(inventario_tienda)
            case "3":
                mostrar_detalle_producto(inventario_tienda)
            case "4":
                analisis_inventario(inventario_tienda)
            case "5":
                informacion_tienda(inventario_tienda)
            case "6":
                print("\n  ¡Hasta pronto! - La Bodega\n")
                break
            case _:
                print("  Opción inválida.")


if __name__ == "__main__":
    main()
