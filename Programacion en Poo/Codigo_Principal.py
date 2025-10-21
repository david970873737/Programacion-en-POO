from Dato_Usuario import Usuario
from Dato_Producto import Producto
from Dato_servidor import Servidor
from Dato_Procesador import Procesador
from Dato_Inexador import indexador
from Dato_Recolector import Recolector
from Dato_Hilo import Hilo
from Dato_Editorial import Editorial
from Dato_Libro import Libro
from Dato_Revista import Revista
from Dato_Articulo_Segunda_Mano import Articulo_segunda_mano
from Dato_Novedades import Novedades
from Dato_Articulo_Online import Articulo_online
#+++++++++++++++++++++++++++ intancia del objeto +++++++++++++++++++++++++++
usuario1 = Usuario("xxxxx ", "xxxxx ", "12345", "Calle Falsa 123", "juanp", "password123")
producto1 = Producto("xxxxx", "xxxxxx ", " xxxxxx", "Salamandra", "1943", "Literatura Infantil")
obj_servidor = Servidor()
procesador1 = Procesador()
dato_indexador = indexador()
dato_recolector = Recolector()
dato_hilo = Hilo()
editorial1 = Editorial("David", "Calle 8 , 1-22", "310687**")

libro1 = Libro("agregaste un libro ")
revista1 = Revista("agregaste una revista ")
articulo_segunda_mano1 = Articulo_segunda_mano("agregaste un articulo der segunda mano ")
novedades1 = Novedades("no hay novedades")
articulo_online1 = Articulo_online("agregaste articulo online")

#+++++++++++++++++++++++++++ llamar metodos normales +++++++++++++++++++++++++++

obj_servidor.muestra_pagina()
obj_servidor.enviar_datos_compra()
obj_servidor.enviar_datos_venta()

print("-----------------------------------------------------------------")

procesador1.mandar_datos_venta()
procesador1.mandar_articulos_online()
procesador1.envia_sugerencia_administrador()
procesador1.modificar_stock()
procesador1.realizar_pago()
procesador1.realizar_cobro()
procesador1.actualizar_catalogo()
procesador1.realiza_busqueda()

print("-----------------------------------------------------------------")

dato_indexador.actualizar_almacen()
dato_indexador.enviar_resultado_busqueda()

print("-----------------------------------------------------------------")

dato_recolector.recolectar_datos()

print("-----------------------------------------------------------------")

dato_hilo.busca_novedades()


#+++++++++++++++++++++++++++ retorno +++++++++++++++++++++++++++
resultado1 = usuario1.enviar_sugerencias("Agreguen más libros ")
print(resultado1)

resultado2 = usuario1.comprar(producto1.titulo)
print(resultado2)

resultado3 = usuario1.realizar_reclamacion("Mal servivio")
print(resultado3)

resultado4 = producto1.ver_catalogo()
print(resultado4)

resultado5 = producto1.vender()
print(resultado5)

resultado6 = producto1.comprar()
print(resultado6)

resultado7 = editorial1.vender(producto1.titulo)
print(resultado7)

resultado8 = libro1.libro
print(resultado8)

resultado9 = revista1.revista
print(resultado9)

resultado10 = articulo_segunda_mano1.articulo_segunda_mano
print(resultado10)

resultado11 = novedades1.cambiar_clasificacion()
print(resultado11)

resultado12 = articulo_online1.publicar()
print(resultado12)
