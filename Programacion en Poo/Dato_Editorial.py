class Editorial:
  def __init__(self,nombre,direccion, telefono ):
    self.nombre = nombre
    self.direccion = direccion
    self.telefono = telefono

  def vender(self, producto):
    return f"la editorial '{self.nombre}' ha vendido el producto: {producto}"
