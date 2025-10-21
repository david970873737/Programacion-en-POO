class Usuario:
  def __init__(self, nombre, apellido, n_cuenta, direccion, login, contrasena): #constructor
    self.nombre = input("Ingrese su nombre: ")
    self.apellido = input("Ingrese su apellido: ")
    self.n_cuenta = n_cuenta              #atributos
    self.direccion = direccion
    self.login = login
    self.contrasena = contrasena

    print("-----------------------------------------------------------------")

  #metodos

  def enviar_sugerencias(self, texto ):
    return f"sugerencia enviada por {self.nombre}: {texto}"

  def leer (self):
    return f"{self.nombre} edta leyendo un articulo "

  def comprar( self, producto ):
    return f"{self.nombre} compro el producto: {producto}"

  def vender(self, producto):
    return f"{self.nombre} puso en venta el producto: {producto}"

  def realizar_reclamacion(self, motivo):
    return f"{self.nombre} realizo una reclamacion: {motivo}"
