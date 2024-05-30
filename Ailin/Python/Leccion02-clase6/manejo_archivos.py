# Declaramos una variable
try:
    archivo = open('prueba.txt', 'w', encoding='utf8')  # la W es write que significa escribir
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras \n')
    archivo.write('Como por ejemplo: acción, ejecución y producción \n')
    archivo.write('Las letras son: \n w write, \n r read, \n a append, \n x crea un archivo \n')
    archivo.write('\n t esta es para texto o text, \n b archivos binarios, \n w+ lee y escribe son iguales r+\n')
    archivo.write('Saludos a todos los estudiantes de la tecnicatura\n')
    archivo.write('Con esto terminamos')
except Exception as e:
    print(e)
finally: #Siempre se ejecuta
    archivo.close() #Con esto se debe cerrar el archivo
# archivo.write('Todo quedo bien'): este es un error