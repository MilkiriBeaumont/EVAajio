from Tecnologia import Tecnologia

class Consola(Tecnologia):
    def __init__(self, nombre_consola, version, voltaje, precio, eficiencia, marca):
        self.__nombre_consola = nombre_consola
        self.__version = version
        self.__voltaje = voltaje
        self.__precio = precio
        self.__eficiencia = eficiencia
        self.__marca = marca

    def calcularDescuento(self, precio):
        """Calcula el descuento que se le aplicará al precio del producto.
        Args:
            precio: El precio original del producto.
        Returns:
            El precio del producto con el descuento aplicado."""
        descuento = 0
        if self.__eficiencia in ["A", "B"]:
            descuento = 0.5
        elif self.__eficiencia in ["C", "D"]:
            descuento = 0.3
        elif self.__eficiencia in ["E", "F"]:
            descuento = 0.1
        if self.__version == "Lite":
            descuento += 0.05
        return precio - (precio * descuento)
