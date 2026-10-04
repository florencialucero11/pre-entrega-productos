# Sistema de gestión básica de productos

Programa de consola en Python para gestionar una lista de productos.
Pre-entrega del proyecto de Inicialización a la programación con Python.

**Autor/a:** Florencia Lucero
**Fecha:** Octubre 2026

## Descripción

El programa permite registrar productos con nombre, categoría y precio,
y consultarlos, buscarlos o eliminarlos desde un menú interactivo.
Los datos se guardan en memoria (en una lista), por lo que se pierden
al cerrar el programa.

## Funcionalidades

1. **Agregar producto:** pide nombre, categoría y precio (entero, sin centavos).
2. **Mostrar productos:** lista todos los productos numerados.
3. **Buscar producto:** busca por nombre, sin distinguir mayúsculas y
   permitiendo coincidencias parciales.
4. **Eliminar producto:** elimina un producto según su número en la lista.
5. **Salir:** termina el programa.


## Cómo ejecutarlo

```
python preentrega.py
```

## Ejemplo de uso

```
Sistema de gestión básica de productos
1. Agregar producto
2. Mostrar productos
3. Buscar producto
4. Eliminar producto
5. Salir
Elegí una opción: 1
Nombre del producto: Tomate
Categoría: Verdura
Precio (sin centavos, ejemplo: 1500): 1200
Producto agregado correctamente.
```

## Estructura de datos

Cada producto es una sublista de tres elementos dentro de una lista principal:

```python
productos = [
    ["Tomate", "Verdura", 1200],
    ["Mouse", "Tecnología", 15000]
]
```

## Validaciones

- El nombre y la categoría no pueden estar vacíos.
- El precio debe ser un número entero mayor a 0.
- La opción del menú debe ser un número del 1 al 5.
- Al eliminar, el número debe existir en la lista.

## Conceptos aplicados

- Listas y sublistas
- Bucles `while` (menú y validaciones) y `for` (recorrido de la lista)
- Condicionales `if / elif / else`
- Validación de entradas con `.strip()` e `.isdigit()`