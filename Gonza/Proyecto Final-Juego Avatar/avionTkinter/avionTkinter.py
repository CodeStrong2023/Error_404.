import tkinter as tk
from tkinter import messagebox
import numpy as np
from conexion import *

class VueloAvionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aerolíneas UTN")
        self.root.geometry("550x300")
        self.root.resizable(False, False)
        root.configure(bg="lightgrey")
        
        self.asiento = np.zeros((4, 25), dtype=int)
        self.PasajerosDNI = ["0"] * 100
        self.PasajerosNombre = ["0"] * 100
        self.ContadorGuardar = [0, 0, 0]
        self.totalPagar = 0
        self.cantidadPasajes = 0
        self.asientosReservados = 0
        
        self.setup_gui()

    def setup_gui(self):
        self.main_frame = tk.Frame(self.root, bg="lightgrey")
        self.main_frame.pack()
        
        tk.Label(self.main_frame, text="", bg="lightgrey").pack()
        
        tk.Label(self.main_frame, text="BIENVENIDOS A AEROLÍNEAS UTN", font=("Helvetica", 14, "bold"), bg="lightgrey").pack()
        tk.Label(self.main_frame, text="SELECCIONE UNA OPCIÓN", font=("Helvetica", 14, "bold"), bg="lightgrey").pack()
        
        tk.Label(self.main_frame, text="", bg="lightgrey").pack()
    
        tk.Button(self.main_frame, text="1- Reservar pasaje", font=("Helvetica", 11, "bold"), height=1, width=15, bg="lightblue" , command=self.reservar_pasaje).pack(pady=2)
        tk.Button(self.main_frame, text="2- Reservar asiento", font=("Helvetica", 11, "bold"), height=1, width=15, bg="lightblue" , command=self.reservar_asiento).pack(pady=2)
        tk.Button(self.main_frame, text="3- Cancelar asiento", font=("Helvetica", 11, "bold"), height=1, width=15, bg="lightblue" , command=self.cancelar_asiento).pack(pady=2)
        tk.Button(self.main_frame, text="4- Mostrar asientos", font=("Helvetica", 11, "bold"), height=1, width=15, bg="lightblue" , command=self.mostrar_asientos).pack(pady=2)
        tk.Button(self.main_frame, text="5- Salir", font=("Helvetica", 11, "bold"), height=1, width=15, bg="lightblue" , command=self.root.quit).pack(pady=2) 
    

    def reservar_pasaje(self):
        self.reserva_window = tk.Toplevel(self.root)
        self.reserva_window.title("Reservar Pasaje")
        
        tk.Label(self.reserva_window, text="!AVISO IMPORTANTE¡", fg="orange", font=("Helvetica", 14, "bold")).pack()
        tk.Label(self.reserva_window, text="Menor 5 años: 100% descuento + $3000 de seguro", font=("Helvetica", 11, "bold")).pack()
        tk.Label(self.reserva_window, text="Mayor 65 años: 50% descuento", font=("Helvetica", 11, "bold")).pack()
        tk.Label(self.reserva_window, text="Se le aplicará el descuento según su destino", font=("Helvetica", 11, "bold")).pack()
        tk.Label(self.reserva_window, text="Opciones de vuelo. Responder con (1 o 2)", font=("Helvetica", 11, "bold")).pack()
        tk.Label(self.reserva_window, text="1_ Destino a: Brasil 15% descuento", font=("Helvetica", 11, "bold")).pack()
        tk.Label(self.reserva_window, text="2_ Destino a: Miami 10% descuento", font=("Helvetica", 11, "bold")).pack()
        
        self.numDestino_var = tk.IntVar()
        tk.Entry(self.reserva_window, textvariable=self.numDestino_var).pack(pady=2)
        
        tk.Button(self.reserva_window, text="Continuar", font=("Helvetica", 11, "bold"), command=self.procesar_reserva).pack()

    def procesar_reserva(self):
        numDestino = self.numDestino_var.get()

        if numDestino not in [1, 2]:
            messagebox.showerror("Error", "Estamos trabajando por el momento con 2 opciones de vuelo. Responder con (1 o 2)")
            return

        self.Miami = 135370
        self.Brasil = 119499

        if numDestino == 1:
            destino_str = "Brasil"
            destino_precio = self.Brasil
            descuento_destino = 15
            tiempo_vuelo = "6h 24m"
        else:
            destino_str = "Miami"
            destino_precio = self.Miami
            descuento_destino = 10
            tiempo_vuelo = "9h 17m"

        self.reserva_window.destroy()

        self.pasaje_window = tk.Toplevel(self.root)
        self.pasaje_window.title("Reservar Pasaje")

        tk.Label(self.pasaje_window, text=f"Destino a {destino_str} = ${destino_precio}", font=("Helvetica", 11, "bold")).pack()
        tk.Label(self.pasaje_window, text=f"Tiempo de vuelo estimado {tiempo_vuelo}.", font=("Helvetica", 11, "bold")).pack()
        tk.Label(self.pasaje_window, text="Ingrese la cantidad de pasajes (máximo 5):", font=("Helvetica", 11, "bold")).pack()

        self.cantidadPasajes_var = tk.IntVar()
        tk.Entry(self.pasaje_window, textvariable=self.cantidadPasajes_var).pack()
        tk.Button(self.pasaje_window, text="Continuar", font=("Helvetica", 11, "bold"), command=lambda: self.procesar_pasajeros(numDestino, destino_precio, descuento_destino)).pack()

    def procesar_pasajeros(self, numDestino, destino_precio, descuento_destino):
        self.cantidadPasajes = self.cantidadPasajes_var.get()

        if self.cantidadPasajes > 5:
            messagebox.showerror("Error", "La cantidad de pasajes ingresada supera el límite permitido.")
            return

        self.contador = 1
        self.totalPagar = 0

        self.pasajero_window = tk.Toplevel(self.root)
        self.pasajero_window.title("Datos de Pasajero")

        self.procesar_pasajero(numDestino, destino_precio, descuento_destino)

    def procesar_pasajero(self, numDestino, destino_precio, descuento_destino):
        if self.contador > self.cantidadPasajes:
            self.pasajero_window.destroy()
            self.seleccionar_horario()
            return

        for widget in self.pasajero_window.winfo_children():
            widget.destroy()

        tk.Label(self.pasajero_window, text=f"Nombre y apellido del pasajero {self.contador}:", font=("Helvetica", 11, "bold")).pack()
        self.nombreCompleto_var = tk.StringVar()
        tk.Entry(self.pasajero_window, textvariable=self.nombreCompleto_var).pack()

        tk.Label(self.pasajero_window, text=f"Documento del pasajero {self.contador}:", font=("Helvetica", 11, "bold")).pack()
        self.DNI_var = tk.StringVar()
        tk.Entry(self.pasajero_window, textvariable=self.DNI_var).pack()

        tk.Label(self.pasajero_window, text=f"Edad del pasajero {self.contador}:", font=("Helvetica", 11, "bold")).pack()
        self.edad_var = tk.IntVar()
        tk.Entry(self.pasajero_window, textvariable=self.edad_var).pack()

        tk.Button(self.pasajero_window, text="Agregar Pasajero", font=("Helvetica", 11, "bold"), command=lambda: self.agregar_pasajero(numDestino, destino_precio, descuento_destino)).pack(pady=2)

    def agregar_pasajero(self, numDestino, destino_precio, descuento_destino):
        nombreCompleto = self.nombreCompleto_var.get()
        DNI = self.DNI_var.get()
        edad = self.edad_var.get()

        if len(DNI) != 8:
            messagebox.showerror("Error", "El documento debe tener 8 dígitos.")
            return

        self.ContadorGuardar[1] += 1
        if self.PasajerosNombre[self.ContadorGuardar[1]] == "0":
            self.PasajerosNombre[self.ContadorGuardar[1]] = nombreCompleto

        if self.PasajerosDNI[self.ContadorGuardar[1]] == "0":
            self.PasajerosDNI[self.ContadorGuardar[1]] = DNI

        if edad <= 5:
            descuento = 100
            seguroVuelo = 3000
        elif edad >= 65:
            descuento = 50
            seguroVuelo = 0
        else:
            descuento = descuento_destino
            seguroVuelo = 0

        costoDescuento = destino_precio * (1 - descuento / 100)
        self.totalPagar += seguroVuelo + costoDescuento

        messagebox.showinfo("Descuento", f"El pasajero {nombreCompleto} tiene un descuento del {descuento}%\nValor pasaje: ${costoDescuento + seguroVuelo}")

        self.contador += 1
        self.procesar_pasajero(numDestino, destino_precio, descuento_destino)

    def seleccionar_horario(self):
        self.horario_window = tk.Toplevel(self.root)
        self.horario_window.title("Seleccionar Horario")

        tk.Label(self.horario_window, text="Horarios disponibles:", font=("Helvetica", 11, "bold")).pack()
        tk.Label(self.horario_window, text="1_ 5:30hs", font=("Helvetica", 11, "bold")).pack()
        tk.Label(self.horario_window, text="2_ 13:10hs", font=("Helvetica", 11, "bold")).pack()
        tk.Label(self.horario_window, text="3_ 15:30hs", font=("Helvetica", 11, "bold")).pack()
        self.Time_var = tk.IntVar()
        tk.Entry(self.horario_window, textvariable=self.Time_var).pack()

        tk.Button(self.horario_window, text="Confirmar", font=("Helvetica", 11, "bold"), command=self.confirmar_reserva).pack(pady=2)

    def confirmar_reserva(self):
        Time = self.Time_var.get()

        if Time == 1:
            horario_str = "5:30hs"
        elif Time == 2:
            horario_str = "13:10hs"
        elif Time == 3:
            horario_str = "15:30hs"
        else:
            messagebox.showerror("Error", "Las opciones eran (1,2 o 3)")
            return

        messagebox.showinfo("Confirmación", f"Su viaje a las {horario_str} sale el próximo Lunes 10/07/2023.\nEl total a pagar es: ${self.totalPagar}")
        self.horario_window.destroy()

    def reservar_asiento(self):
        self.reserva_asiento_window = tk.Toplevel(self.root)
        self.reserva_asiento_window.title("Reservar Asiento")

        tk.Label(self.reserva_asiento_window, text="Ingrese la fila del asiento (1-4):", font=("Helvetica", 11, "bold")).pack()
        self.fila_var = tk.IntVar()
        tk.Entry(self.reserva_asiento_window, textvariable=self.fila_var).pack()

        tk.Label(self.reserva_asiento_window, text="Ingrese el número de asiento (1-25):", font=("Helvetica", 11, "bold")).pack()
        self.asiento_var = tk.IntVar()
        tk.Entry(self.reserva_asiento_window, textvariable=self.asiento_var).pack()

        tk.Button(self.reserva_asiento_window, text="Reservar", font=("Helvetica", 11, "bold"), command=self.procesar_reserva_asiento).pack(pady=2)

    def procesar_reserva_asiento(self):
        if self.asientosReservados >= self.cantidadPasajes:
            messagebox.showerror("Error", "No puede reservar más asientos que la cantidad de pasajes reservados.")
            return

        fila = self.fila_var.get() - 1
        asiento = self.asiento_var.get() - 1

        if not (0 <= fila < 4) or not (0 <= asiento < 25):
            messagebox.showerror("Error", "Número de fila o asiento inválido.")
            return

        if self.asiento[fila][asiento] == 0:
            self.asiento[fila][asiento] = 1
            self.asientosReservados += 1
            messagebox.showinfo("Éxito", f"Asiento {asiento + 1} en fila {fila + 1} reservado con éxito.")
        else:
            messagebox.showerror("Error", "El asiento ya está reservado.")

        self.reserva_asiento_window.destroy()

    def cancelar_asiento(self):
        self.cancelar_asiento_window = tk.Toplevel(self.root)
        self.cancelar_asiento_window.title("Cancelar Asiento")

        tk.Label(self.cancelar_asiento_window, text="Ingrese la fila del asiento a cancelar (1-4):", font=("Helvetica", 11, "bold")).pack()
        self.fila_cancelar_var = tk.IntVar()
        tk.Entry(self.cancelar_asiento_window, textvariable=self.fila_cancelar_var).pack()

        tk.Label(self.cancelar_asiento_window, text="Ingrese el número de asiento a cancelar (1-25):", font=("Helvetica", 11, "bold")).pack()
        self.asiento_cancelar_var = tk.IntVar()
        tk.Entry(self.cancelar_asiento_window, textvariable=self.asiento_cancelar_var).pack()

        tk.Button(self.cancelar_asiento_window, text="Cancelar", font=("Helvetica", 11, "bold"), command=self.procesar_cancelar_asiento).pack(pady=2)

    def procesar_cancelar_asiento(self):
        fila = self.fila_cancelar_var.get() - 1
        asiento = self.asiento_cancelar_var.get() - 1

        if not (0 <= fila < 4) or not (0 <= asiento < 25):
            messagebox.showerror("Error", "Número de fila o asiento inválido.")
            return

        if self.asiento[fila][asiento] == 1:
            self.asiento[fila][asiento] = 0
            messagebox.showinfo("Éxito", f"Asiento {asiento + 1} en fila {fila + 1} cancelado con éxito.")
        else:
            messagebox.showerror("Error", "El asiento no estaba reservado.")

        self.cancelar_asiento_window.destroy()

    def mostrar_asientos(self):
        self.asientos_window = tk.Toplevel(self.root)
        self.asientos_window.title("Mostrar Asientos")
        for i in range(4):
            fila_text = f"Fila {i + 1}: " + " ".join(str(x) for x in self.asiento[i])
            tk.Label(self.asientos_window, text=fila_text).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = VueloAvionApp(root)
    root.mainloop()
