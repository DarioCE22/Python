usuario_correcto = "admin"
contrasena_correcta = "1234"

usuario = input("Introduce tu nombre de usuario: ")
contrasena = input("Introduce tu contraseña: ")

if usuario == usuario_correcto and contrasena == contrasena_correcta:
    print("Acceso concedido")
else:
    print("Acceso denegado")
