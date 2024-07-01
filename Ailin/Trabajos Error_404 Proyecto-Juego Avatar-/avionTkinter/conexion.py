import mysql.connector
from avionTkinter import*
import tkinter as tk
import numpy as np

class VueloAvionApp:

    def __init__(self, root):
        self.root = root
        self.asiento = [[0]*25 for _ in range(4)]
        self.asientosReservados = 0
        self.cantidadPasajes = 100

        self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='quito1991',
                db='aerolineas_utn',
                )
        self.cursor = self.conexion.cursor()

        self.crear_tabla_reservas()

        # Resto del código omitido por brevedad
    def crear_tabla_reservas(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS reservas (nombre Completo VARCHAR(50),DNI VARCHAR(8),edad INT ,numDestino INT,Time INT,fila INT,asiento INT )")
    def procesar_reserva_asiento(self, nombreCompleto, DNI, edad, numDestino, Time, fila, asiento):
        self.conexion.autocommit()
        # Resto del método procesar_reserva_asiento()

        # Insertar datos en la base de datos MySQL
        sql = "insert into reservas values (%s, %s, %s, %s, %s, %s, %s)"
        valores = ( nombreCompleto, DNI, edad, numDestino, Time, fila, asiento)
        self.cursor.execute(sql, valores)
        self.conexion.commit()

    def procesar_cancelar_asiento(self, fila, asiento):
        # Resto del método procesar_cancelar_asiento()

        # Eliminar datos de la base de datos MySQL
        sql = 'DELETE FROM reservas WHERE fila = %s AND asiento = %s'
        val = (fila, asiento)
        self.cursor.execute(sql, val)
        self.conexion.commit()      


# Resto de tu código
if __name__ == "__main__":
    root = tk.Tk()
    app = VueloAvionApp(root)
    root.mainloop()