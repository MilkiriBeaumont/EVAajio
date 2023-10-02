from Tecnologia import Tecnologia
class Tv(Tecnologia):
    def __init__(self, voltaje, precio, eficiencia, marca, tamano, descuento):
        self.__voltaje = voltaje
        self.__precio = precio
        self.__eficiencia = eficiencia
        self.__marca = marca
        self.__tamano = tamano

    def imprimirCaracteristicas(self, precio, descuento):
        """Imprime las caracteristicas del objeto."""
        print("Marca:", self.__marca)
        print("Voltaje:", self.__voltaje)
        print("Eficiencia:", self.__eficiencia)
        print("Precio:", self.__precio)
        print("tamano:", self.__tamano)
        print("Descuento aplicado:", self.des)
        print("Valor total:", self.__precio - (precio * descuento))