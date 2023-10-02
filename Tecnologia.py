class Tecnologia:
    def __init__(self, voltaje, precio, eficiencia, marca):
        self.__voltaje = voltaje
        self.__precio = precio
        self.__eficiencia = eficiencia
        self.__marca = marca

    def imprimirCaracteristicas(self):
        """Imprime las caracteristicas del objeto."""
        print("Marca:", self.__marca)
        print("Voltaje:", self.__voltaje)
        print("Eficiencia:", self.__eficiencia)
        print("Precio:", self.__precio)
        
    def calcularDescuento(self,precio):
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
            return precio - (precio * descuento)

