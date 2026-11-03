"""
Analizador de notas: calcula el promedio de tres calificaciones.

Explicación del error y su corrección:
- Qué hacía mal el programa: calculaba el promedio como 'nota_1 + nota_2 + nota_3 / 3'.
  Debido a la precedencia de operadores en Python, primero dividía 'nota_3 / 3' y al
  resultado le sumaba 'nota_1' y 'nota_2', dando un promedio incorrecto superior al real.
- Cómo se corrigió: tras inspeccionar la variable 'promedio' con un breakpoint en el
  depurador de IntelliJ, se agruparon las sumas entre paréntesis '(nota_1 + nota_2 + nota_3) / 3'
  para que la suma total se realice antes de dividir entre 3.
"""

# Pedimos las tres notas al usuario y las convertimos a decimal (float)
nota_1 = float(input("Introduce la primera nota: "))
nota_2 = float(input("Introduce la segunda nota: "))
nota_3 = float(input("Introduce la tercera nota: "))

# Cálculo con el error lógico (comentado tras depurar en IntelliJ):
# promedio = nota_1 + nota_2 + nota_3 / 3

# Cálculo corregido usando paréntesis para respetar el orden de las operaciones
promedio = (nota_1 + nota_2 + nota_3) / 3

# Mostramos el promedio final por pantalla
print(f"El promedio de las tres notas es: {promedio}")