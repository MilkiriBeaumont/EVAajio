from Tecnologia import Tecnologia
from Tv import Tv
from Consola import Consola
from Bicicleta import Bicicleta


def menu():
    productos = []

    while True:
        print("\nMenú:")
        print("1. Registrar Tv")
        print("2. Registrar Consola")
        print("3. Registrar Bicicleta")
        print("4. Cotizar producto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_tv(productos)
        elif opcion == '2':
            registrar_consola(productos)
        elif opcion == '3':
            registrar_bicicleta(productos)
        elif opcion == '4':
            cotizar_producto(productos)
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor seleccione una opción válida.")

class Producto(Tecnologia):
    def __init__(self, marca, precio):
        self.marca = marca
        self.precio = precio

class TV(Producto):
    def __init__(self, marca, precio, voltaje, eficiencia, tamano):
        super().__init__(marca, precio)
        self.voltaje = voltaje
        self.eficiencia = eficiencia
        self.tamano = tamano

class Consola(Producto):
    def __init__(self,nombre_consola, marca, precio, voltaje, eficiencia,  version):
        super().__init__(marca, precio)
        self.nombre_consola = nombre_consola
        self.voltaje = voltaje
        self.eficiencia = eficiencia
        self.version = version

class Bicicleta(Producto):
    def __init__(self, marca, precio, peso, aro):
        super().__init__(marca, precio)
        self.peso = peso
        self.aro = aro

def cotizar_producto(productos):
    print("\nCotización de Producto:")
    tipo_producto = input("Ingrese el tipo de producto a cotizar (TV, Consola, Scooter, Bicicleta): ").strip().lower()

    if tipo_producto == 'tv':
        cotizar_tv(productos)
    elif tipo_producto == 'consola':
        cotizar_consola(productos)
    elif tipo_producto == 'bicicleta':
        cotizar_bicicleta(productos)
    else:
        print("Tipo de producto no válido. Por favor, ingrese un tipo válido.")


def cotizar_tv(productos):
    print("\nCotización de TV:")
    if not productos:
        print("No hay TVs registradas.")
        return

    print("Seleccione una TV para cotizar:")
    for i, producto in enumerate(productos):
        if isinstance(producto, TV):
            print(f"{i + 1}. Marca: {producto.marca}, Precio: ${producto.precio:.2f}")

    seleccion = input("Ingrese el número de la TV que desea cotizar: ")

    try:
        seleccion = int(seleccion)
        if 1 <= seleccion <= len(productos) and isinstance(productos[seleccion - 1], TV):
            tv = productos[seleccion - 1]
            print(f"Marca: {tv.marca}, Precio: ${tv.precio:.2f}")
        else:
            print("Selección no válida.")
    except ValueError:
        print("Ingrese un número válido.")


def cotizar_consola(productos):
    print("\nCotización de consolas:")
    if not productos:
        print("No hay consolas registradas.")
        return

    print("Seleccione una consola para cotizar:")
    for i, producto in enumerate(productos):
        if isinstance(producto, TV):
            print(f"{i + 1}. Marca: {producto.marca}, Precio: ${producto.precio:.2f}")

    seleccion = input("Ingrese el número de la consola que desea cotizar: ")

    try:
        seleccion = int(seleccion)
        if 1 <= seleccion <= len(productos) and isinstance(productos[seleccion - 1], Consola):
            consola = productos[seleccion - 1]
            print(f"Marca: {consola.marca}, Precio: ${consola.precio:.2f}")
        else:
            print("Selección no válida.")
    except ValueError:
        print("Ingrese un número válido.")


def cotizar_bicicleta(productos):
    print("\nCotización de bicicleta:")
    if not productos:
        print("No hay bicicletas registradas.")
        return

    print("Seleccione una bicileta para cotizar:")
    for i, producto in enumerate(productos):
        if isinstance(producto, TV):
            print(f"{i + 1}. Marca: {producto.marca}, Precio: ${producto.precio:.2f}")

    seleccion = input("Ingrese el número de la bicicleta que desea cotizar: ")

    try:
        seleccion = int(seleccion)
        if 1 <= seleccion <= len(productos) and isinstance(productos[seleccion - 1], Bicicleta):
            bicicleta = productos[seleccion - 1]
            print(f"Marca: {bicicleta.marca}, Precio: ${bicicleta.precio:.2f}")
        else:
            print("Selección no válida.")
    except ValueError:
        print("Ingrese un número válido.")

# Las funciones cotizar_consola y cotizar_bicicleta se implementan de manera similar

def registrar_tv(productos):
    print("\nRegistro de TV:")
    marca = input("Marca: ")
    voltaje = input("Voltaje: ")
    eficiencia = input("Eficiencia (A, B, C, D, E, F): ").upper()
    precio = float(input("Precio: $"))
    tamano = input("Tamaño: ")

    tv = TV(marca, precio, voltaje, eficiencia, tamano)
    productos.append(tv)

    print("\nTV registrada con éxito.")

def registrar_consola(productos):
    print("\nRegistro de Consola:")
    marca = input("Marca: ")
    voltaje = input("Voltaje: ")
    nombre_consola = input("nombre_consola: ")
    eficiencia = input("Eficiencia (A, B, C, D, E, F): ").upper()
    precio = float(input("Precio: $"))
    tamano = input("Tamaño: ")

    consola = Consola(marca, precio, voltaje, eficiencia, tamano,nombre_consola)
    productos.append(consola)

    print("\nConsola registrada con éxito.")

def registrar_bicicleta(productos):
    print("\nRegistro de Bicicleta:")
    marca = input("Marca: ")
    peso = input("Peso: ")
    precio = float(input("Precio: $"))
    aro = input("Aro: ")

    bicicleta = Bicicleta(marca, precio, peso, aro)
    productos.append(bicicleta)

    print("\nBicicleta registrada con éxito.")


# Las funciones registrar_consola y registrar_bicicleta se implementan de manera similar

if __name__ == "__main__":
    print("Bienvenido al sistema de registro y cotización de productos de supermercado.")
    menu()