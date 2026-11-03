"""
Este programa solicita un número entero al usuario por teclado
y muestra por pantalla su tabla de multiplicar del 1 al 10.
"""

# Solicitamos el número al usuario y lo convertimos a tipo entero (int)
numero_tabla = int(input("Introduce un número: "))

# Mostramos el encabezado de la tabla
print(f"Tabla de multiplicar del {numero_tabla}:")

# Recorremos los números del 1 al 10 para calcular y mostrar cada multiplicación
for multiplicador in range(1, 11):
    resultado_multiplicacion = numero_tabla * multiplicador
    print(f"{numero_tabla} x {multiplicador} = {resultado_multiplicacion}")