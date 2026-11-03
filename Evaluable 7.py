"""
Este programa recorre una lista de nombres y muestra por pantalla
únicamente aquellos que no empiezan por la letra 'A' (mayúscula o minúscula),
utilizando la sentencia continue para saltar las coincidencias.
"""

# Definimos una lista con 6 nombres
lista_nombres = ["Ana", "Pedro", "Alba", "Lucía", "alberto", "Carlos"]

# Recorremos cada nombre de la lista
for nombre in lista_nombres:
    # Obtenemos la primera letra del nombre usando el bucle for sobre el string
    primera_letra = ""
    for letra in nombre:
        primera_letra = letra
        break

    # Si empieza por 'A' o 'a', saltamos a la siguiente iteración con continue
    if primera_letra == "A" or primera_letra == "a":
        continue

    # Mostramos el nombre si no fue saltado
    print(nombre)