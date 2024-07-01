from producto import producto


class orden:
    contador_ordenes = 0

    def __init__(self, productos):
        orden.contador_ordenes += 1
        self.id_orden = orden.contador_ordenes
        self._productos = list(productos)

    def agregar_producto(self, producto):
        self._productos.append(producto)

def calcular_total(self):
    total = 0
    for producto in self._productos:
        total += producto.precio
    return total

def __str__(self):
    productos_str = ''
    for producto in self._productos:
        productos_str += producto.__str__()+'|'
    return f'orden: {self.id_orden}, \nproducto: {productos_str}'


if __name__ == '__main__':
    producto1 = producto('camiseta', 100.00)
    producto2 = producto('pantalon', 150.00)
    producto3 = producto('medias', 20.00)
    productos1 = [producto1, producto2, producto3]
    productos2 = [producto2, producto3]
    orden1 = orden(productos1)
    print(orden1)
    orden2 =orden(productos2)
    print(orden2)
