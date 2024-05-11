class producto:
    contador_productos = 0

    def __init__(self, nombre, precio):
        producto.contador_productos += 1
        self._id_producto = producto.contador_productos
        self._nombre = nombre
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f'id producto: {self._id_producto}, nombre: {self._nombre}, precio: {self._precio}'


if __name__ == ' main ':
    producto1 = producto('camiseta', 100.00)
    print(producto1)
    producto2 = producto('pantalon', 150.00)
    print(producto2)
    producto3 = producto('medias', 20.00)
    print(producto3)
    producto4 = producto('gorro', 70.00)
    print(producto4)
