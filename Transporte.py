class transporte():
  def __init__(self, costodespacho):
    self.__costodespacho = costodespacho


def calcularCostoDespacho(self):
  """Calcula el costo del despacho del producto.
  Args:
    peso: El peso del producto en kilogramos.
  Returns:
    El costo del despacho del producto.
  """
  costo_base = 4000
  costo_por_kg = 1000
  return costo_base + (costo_por_kg * self.peso)