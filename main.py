# La empresa en la que trabajas recibe una gran cantidad de materias primas y otros productos en su inventario,
# los cuales son registrados y manejados en hojas de papel que describen nombres, cantidades, precios, tipos y
# tamaños de cada producto que entra y sale. Recientemente se perdieron algunas hojas y se tomó la decisión de
# digitalizar este proceso. Dado esto, se te pide que desarrolles un programa en Python, en el cual, la persona
# encargada de registrar entradas y salidas de inventarios, mediante la terminal del sistema operativo pueda
# hacer estos registros fácilmente.

# La tarea se deberá llevar a cabo utilizando funciones para añadir nuevos artículos, actualizar cantidades y
# buscar artículos específicos basándose en varios criterios. Se deberán utilizar funciones lambda para ordenar
# el inventario en función de diferentes atributos, como ordenar los artículos por nombre, cantidad o precio.
# Además, se deberán emplear funciones anidadas para gestionar operaciones complejas, como generar informes de
# inventario o calcular el valor total del inventario.

# Se deberá subir este archivo de Python a un repositorio Github, junto con un archivo README.md que explique
# cómo utilizar el programa.

# Se evaluará el uso de funciones y funciones lambda para agregar (con diferentes datos incluyendo fecha con la
# paquetería datetime), editar, leer, y borrar productos del inventario, que todo funcione correctamente y que
# contenga el archivo README

# Adicionalmente hacer 3 funciones mas a gusto propio

productos = []
# nombres, cantidades, precios, tipos y tamaños de cada producto que entra y sale
# añadir, actualizar, buscar, ordenar por nombre, cantidad o precio.
# generar informe de inventario o calcular total del inventario


def add_producto():
    nombre = input("Enter producto nombre: ")
    cantidad = input("Enter producto cantidad: ")
    precio = input("Enter producto precio: ")
    tipo = input("Enter producto tipo: ")
    tamaño = input("Enter producto tamaño: ")
    producto = {
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio,
        "tipo": tipo,
        "tamaño": tamaño,
    }
    productos.append(producto)
    print("producto added.")


def update_producto():
    nombre = input("Enter producto nombre to update: ")
    for producto in productos:
        if producto["nombre"] == nombre:
            cantidad = input("Enter new cantidad: ")
            precio = input("Enter new precio: ")
            producto["cantidad"] = cantidad
            producto["precio"] = precio
            print("producto updated.")
            return
    print("producto not found.")


def search_producto():
    name = input("Enter producto nombre to search: ")
    filtered_productos = list(
        filter(lambda producto: name.lower() in producto["nombre"].lower(), productos)
    )
    if len(filtered_productos) > 0:
        print(filtered_productos)
    else:
        print("No productos found.")


def sort_producto():
    option = input("Sort by : \n1. nombre\n2.precio\n3.tipo\nEnter Option: ")
    if option == "1":
        sorted_productos = list(
            sorted(productos, key=lambda producto: producto["nombre"])
        )
    elif option == "2":
        sorted_productos = list(
            sorted(productos, key=lambda producto: producto["precio"])
        )
    elif option == "3":
        sorted_productos = list(
            sorted(productos, key=lambda producto: producto["tipo"])
        )
    else:
        print("Invalid option.")
        return
    if len(sorted_productos) > 0:
        print(sorted_productos)
    else:
        print("No productos found.")


def delete_producto():
    nombre = input("Enter producto nombre to delete: ")
    for producto in productos:
        if producto["nombre"] == nombre:
            producto["nombre"].pop()
            print("producto deleted.")
            return
    print("producto not found.")


def get_producto():
    print(
        "| {:10} | {:10}| {:10} | {:10}| {:10}".format(
            "Nombre", "Precio", "Tipo", "Tamaño", "Cantidad"
        )
    )
    for producto in productos:
        print(
            "| {:10} | {:10}| {:10} | {:10}| {:10}".format(
                producto["nombre"],
                producto["precio"],
                producto["tipo"],
                producto["tamaño"],
                producto["cantidad"],
            )
        )


def total_producto():
    total = 0
    for producto in productos:
        total += int(producto["cantidad"])
    print(f"Inventario de materia prima, con un total de: {total} productos.")


def costomer_menu():
    while True:
        print("\n-- Producto Management System ---")
        print("1. Add producto")
        print("2. Update producto")
        print("3. Search producto")
        print("4. Sort productos")
        print("5. Delete producto")
        print("6. Get productos")
        print("7. Total del inventario")
        print("8. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_producto()
        elif choice == 2:
            update_producto()
        elif choice == 3:
            search_producto()
        elif choice == 4:
            sort_producto()
        elif choice == 5:
            delete_producto()
        elif choice == 6:
            get_producto()
        elif choice == 7:
            total_producto()
        elif choice == 8:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again")


costomer_menu()
