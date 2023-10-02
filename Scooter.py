from Tecnologia import Tecnologia

class Scooter(Tecnologia):
    def __init__(self, aro, velocidad, peso, eficiencia):
        self.__aro = aro
        self.__velocidad = velocidad
        self.__peso = peso
        self.__eficiencia = eficiencia

def calcularDespacho(self, distancia):
    costo = self.costodespachobase
    # Agregar un recargo por distancia
    if distancia > 100:
        costo += (distancia - 100) * 0.5
    return costo