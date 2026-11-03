num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operacion = input("Elige operación (suma, resta, multiplicacion, division): ")

if operacion == "suma":
    print(f"Resultado: {num1 + num2}")
elif operacion == "resta":
    print(f"Resultado: {num1 - num2}")
elif operacion == "multiplicacion":
    print(f"Resultado: {num1 * num2}")
elif operacion == "division":
    print(f"Resultado: {num1 / num2}")
else:
    print("Operación no reconocida")
