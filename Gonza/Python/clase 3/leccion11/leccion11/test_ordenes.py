from orden import orden
from producto import producto

producto1 = producto('camiseta', 100.00)
producto2 = producto('pantalon', 150.00)
producto3 = producto('medias', 20.00)
producto4 = producto('gorra', 80.00)
producto5 = producto('campera', 200.00)

productos1 = [producto1, producto2, producto3]
productos2 = [producto4, producto3]
orden1 = orden(productos1)
orden1.agregar_producto(producto5)
print(orden1)
print(f'total de la orden1: {orden1.calcular_total()}')
orden2 = orden(productos2)
orden2.agregar_producto(producto1)
print(orden2)
print(f'total de la orden2 : {orden2.calcular_total()}')
