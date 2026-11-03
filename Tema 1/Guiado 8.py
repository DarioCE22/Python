# --- VERSIÓN CON ERROR LÓGICO (para probar en modo Debug) ---
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Error lógico: realiza primero num2 / 2 y luego suma num1
resultado_erroneo = num1 + num2 / 2
print(f"Resultado con error lógico: {resultado_erroneo}")

# --- VERSIÓN CORREGIDA ---
# Se añaden paréntesis para sumar ambos números antes de dividir entre 2
resultado_correcto = (num1 + num2) / 2
print(f"Resultado corregido: {resultado_correcto}")
