from Transporte import transporte
class Bicicleta(transporte):
    def __init__(self, peso, aro, precio, marca):
        self.__peso = peso
        self.__aro = aro
        self.__precio = precio
        self.__marca = marca

    def calcularDespacho(self):
        """Calcula el costo del despacho del producto.
        Args:
            peso: El peso del producto en kilogramos.
        Returns:
            El costo del despacho del producto."""
        costo_base = 4000
        costo_por_kg = 1000
        return costo_base + (costo_por_kg * self.__peso) + (costo_base * 0.1)
    
    def imprimirCaracteristicas(self):
        """Imprime las caracteristicas del objeto."""
        super().imprimirCaracteristicas()
        print("Costo de despacho:", self.calcularDespacho())

    def calcularCostoDespacho(self):
        """Calcula el costo del despacho del producto.
        Args:
            peso: El peso del producto en kilogramos.
        Returns:
            El costo del despacho del producto."""
        return self.__peso * 400

