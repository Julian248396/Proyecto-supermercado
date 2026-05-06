# Sistema de Inventario — La Bodeguita

**La Bodeguita** es un sistema de gestión de inventario para una tienda local, desarrollado en Python. Permite administrar productos, consultar información detallada, analizar el inventario y gestionar datos de la tienda de forma sencilla desde la consola.
![image alt](https://github.com/Julian248396/Proyecto-supermercado/blob/ada224da1bad0b8020c04673d9b455d79d599219/sadwf.png) 

---

---

## ⚙️ Requisitos

- Python 3.10 o superior (se utiliza `match` / `case`)
- No requiere librerías externas

---

## ▶️ Cómo ejecutar

```bash
python Sistema_de_inventario_para_supermercado.py
```

Al ejecutar, se abrirá el menú principal desde el cual se accede a todos los módulos.

---

## 🗂️ Módulos del sistema

### 1. Gestión de Productos (CRUD)
Permite crear, consultar, modificar y eliminar productos del inventario.

### 2. Ver Inventario Completo
Muestra todos los productos con su nombre, categoría, precio, cantidad y estado (Disponible / Agotado).

### 3. Ver Detalle de un Producto
Muestra la información completa de un producto: unidad de medida, etiquetas, historial de precios con promedio, y datos del proveedor.

### 4. Análisis del Inventario
Permite consultar categorías únicas, productos agotados, y el producto más caro y más barato.

### 5. Información de la Tienda
Muestra los datos generales de La Bodeguita y permite consultar datos individuales por índice.

---

## 🧱 Estructura de un Producto

Cada producto en el inventario maneja las siguientes estructuras de datos:

| Campo             | Tipo       | Descripción                              |
|------------------|------------|------------------------------------------|
| `nombre`         | `str`      | Nombre completo del producto             |
| `categoria`      | `str`      | Categoría a la que pertenece             |
| `precio`         | `float`    | Precio actual                            |
| `cantidad`       | `int`      | Unidades disponibles en inventario       |
| `unidad_medida`  | `tuple`    | (tipo, abreviatura, referencia)          |
| `historial_precios` | `list` | Lista de precios anteriores              |
| `etiquetas`      | `set`      | Características del producto             |
| `proveedor`      | `dict`     | Diccionario anidado con nombre, ciudad y teléfono |

---

## 🔧 Funciones del sistema

| Función                      | Tipo       | Descripción                                              |
|-----------------------------|------------|----------------------------------------------------------|
| `mostrar_menu()`            | Auxiliar   | Dibuja cualquier menú con título y opciones numeradas    |
| `calcular_promedio_precios()` | Auxiliar | Calcula el promedio de una lista de precios              |
| `mostrar_inventario()`      | Principal  | Lista todos los productos con información básica         |
| `mostrar_detalle_producto()` | Principal | Muestra toda la info de un producto incluyendo datos anidados |
| `gestionar_productos()`     | CRUD       | Agregar, consultar, modificar y eliminar productos       |
| `analisis_inventario()`     | Principal  | Análisis general del inventario                          |
| `informacion_tienda()`      | Principal  | Muestra los datos de la tienda                           |
| `main()`                    | Entrada    | Inicializa el inventario y lanza el menú principal       |

---

## 🏪 Información de la Tienda

| Campo      | Valor             |
|-----------|-------------------|
| Nombre    | La Bodeguita      |
| Dirección | Vallecito, Tolima |
| Tipo      | Tienda Local      |
| Año       | 2020              |

---

## 👨‍💻 Autores

Proyecto desarrollado para la asignatura de **Programación de Computadores**.
