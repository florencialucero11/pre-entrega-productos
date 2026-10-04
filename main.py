productos = []

while True:
    print("\nSistema de gestión básica de productos")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Elegí una opción: ").strip()

    if opcion == "1":
        while True:
            nombre = input("Nombre del producto: ").strip()
            if nombre != "":
                break
            print("El nombre no puede estar vacío.")

        while True:
            categoria = input("Categoría: ").strip()
            if categoria != "":
                break
            print("La categoría no puede estar vacía.")

        while True:
            precio_texto = input("Precio (sin centavos): ").strip()
            if precio_texto.isdigit() and int(precio_texto) > 0:
                precio = int(precio_texto)
                break
            print("Ingresá un número entero mayor a 0.")

        productos.append([nombre, categoria, precio])
        print("Producto agregado correctamente.")

    elif opcion == "2":
        if len(productos) == 0:
            print("No hay productos registrados.")
        else:
            print("\n--- Lista de productos ---")
            for i in range(len(productos)):
                producto = productos[i]
                print(f"{i + 1}. Nombre: {producto[0]} | Categoría: {producto[1]} | Precio: ${producto[2]}")

    elif opcion == "3":
        busqueda = input("Ingresá el nombre a buscar: ").strip().lower()
        if busqueda == "":
            print("La búsqueda no puede estar vacía.")
        else:
            encontrados = False
            for i in range(len(productos)):
                producto = productos[i]
                if busqueda in producto[0].lower():
                    print(f"Nombre: {producto[0]} | Categoría: {producto[1]} | Precio: ${producto[2]}")
                    encontrados = True
            if not encontrados:
                print("No se encontraron resultados.")

    elif opcion == "4":
        if len(productos) == 0:
            print("No hay productos para eliminar.")
        else:
            for i in range(len(productos)):
                producto = productos[i]
                print(f"{i + 1}. {producto[0]} | {producto[1]} | ${producto[2]}")

            numero_texto = input("Número del producto a eliminar: ").strip()
            if numero_texto.isdigit():
                numero = int(numero_texto)
                if 1 <= numero <= len(productos):
                    eliminado = productos.pop(numero - 1)
                    print(f"Se eliminó: {eliminado[0]}")
                else:
                    print("Ese número no existe en la lista.")
            else:
                print("Ingresá un número válido.")

    elif opcion == "5":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Elegí un número del 1 al 5.")