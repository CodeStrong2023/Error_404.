from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

teclado1 = Teclado('Asus', 'USB')
monitor1 = Monitor('Asus', '24"')
raton1 = Raton('Asus', 'USB')
computadora1 = Computadora('Lenovo', monitor1, teclado1, raton1)

teclado2 = Teclado('Asus', 'USB')
monitor2 = Monitor('Zowie', '27"')
raton2 = Raton('Logitech', 'Wireless')
computadora2 = Computadora('AlienWare', monitor1, teclado1, raton1)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
print(orden1)

teclado3 = Teclado('Asus', 'USB')
monitor3 = Monitor('Asus', '24"')
raton3 = Raton('Asus', 'USB')
computadora3 = Computadora('Lenovo', monitor3, teclado3, raton3)

teclado4 = Teclado('Trust', 'USB')
monitor4 = Monitor('Apple', '27"')
raton4 = Raton('Redragón', 'Wireless')
computadora4 = Computadora('AlienWare', monitor4, teclado4, raton4)

computadoras2 = [computadora3, computadora4]
orden2 = Orden(computadoras1)
orden2.agregar_computadora(computadora2)
print(orden2)







