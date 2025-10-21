class Producto:
  def __init__(self,precio, titulo, autor, editorial, anio_edicion, preferencias): #constructor
    self.precio = input("Ingrese el precio del producto: ")
    self.titulo = input("Ingrese el titulo del producto: ")
    self.autor = input("ingrese el nombre del autor")                   #atributos
    self.editorial = editorial
    self.anio_edicion = anio_edicion
    self.preferencias = preferencias

  #metodos

  def vender(self):
    return f"el producto '{self.titulo}' ha sido vendido"

  def comprar(self):
    return f"el producto '{self.titulo}' fue comprado exitosamente"

  def ver_catalogo(self):
    return f"titulo: {self.titulo}  | autor: {self.autor} | precio: ${self.precio}"