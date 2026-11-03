"""
Sistema de registro e inicio de sesión interactivo en consola.
Permite registrar un usuario validando los requisitos de su identificador y
la seguridad de su contraseña, e iniciar sesión con un límite máximo de 3 intentos.
"""

# Variables globales para almacenar las credenciales del usuario registrado
identifier = ""
password = ""

# Variable de control para mantener activo el menú principal
ejecutando_programa = True

while ejecutando_programa:
    opcion = input("\n¿Qué quieres hacer? [1] Registrarse [2] Iniciar sesión [3] Salir: ")

    # OPCIÓN 1: REGISTRO DE USUARIO
    if opcion == "1":
        # 1.1 Bucle de validación del identificador (email)
        identificador_valido = False
        while not identificador_valido:
            candidato_id = input("Introduce un nombre de usuario (email): ")

            longitud_id = 0
            tiene_arroba = False
            tiene_simbolo_prohibido = False

            # Recorremos carácter a carácter para contar longitud y buscar símbolos
            for caracter in candidato_id:
                longitud_id += 1
                if caracter == "@":
                    tiene_arroba = True

                # Comprobamos que no contenga símbolos especiales prohibidos
                for simbolo in "!#$%&*?":
                    if caracter == simbolo:
                        tiene_simbolo_prohibido = True

            # Comprobamos si contiene alguna de las extensiones válidas (.com, .es, .net)
            tiene_extension = False
            ultimos_4 = ""
            ultimos_3 = ""
            posicion_actual = 0

            for caracter in candidato_id:
                posicion_actual += 1
                if posicion_actual > longitud_id - 4:
                    ultimos_4 = ultimos_4 + caracter
                if posicion_actual > longitud_id - 3:
                    ultimos_3 = ultimos_3 + caracter

            if ultimos_4 == ".com" or ultimos_4 == ".net" or ultimos_3 == ".es":
                tiene_extension = True

            # Verificamos todas las reglas del identificador
            if longitud_id >= 3 and tiene_arroba and tiene_extension and not tiene_simbolo_prohibido:
                identifier = candidato_id
                identificador_valido = True
            else:
                print(
                    "Identificador inválido X. Debe tener al menos 3 caracteres, "
                    "contener '@', terminar en .com, .es o .net y no incluir símbolos especiales."
                )

        # 1.2 Bucle de validación de la contraseña
        contrasena_valida = False
        while not contrasena_valida:
            candidata_pass = input("Introduce una contraseña: ")

            longitud_pass = 0
            tiene_mayuscula = False
            tiene_numero = False
            tiene_simbolo = False

            # Analizamos cada carácter de la contraseña
            for caracter in candidata_pass:
                longitud_pass += 1
                if "A" <= caracter <= "Z":
                    tiene_mayuscula = True
                elif "0" <= caracter <= "9":
                    tiene_numero = True
                else:
                    for simbolo in "!@#$%&*?":
                        if caracter == simbolo:
                            tiene_simbolo = True

            # Verificamos si cumple los 4 requisitos de seguridad
            if longitud_pass >= 8 and tiene_mayuscula and tiene_numero and tiene_simbolo:
                password = candidata_pass
                contrasena_valida = True
                print("Usuario registrado con éxito")
            else:
                print(
                    "Contraseña insegura X. Debe tener al menos 8 caracteres, "
                    "una mayúscula, un número y un símbolo."
                )

    # OPCIÓN 2: INICIO DE SESIÓN
    elif opcion == "2":
        if identifier == "":
            print("Aún no hay ningún usuario registrado. Por favor, regístrate primero.")
        else:
            usuario_input = input("Introduce tu usuario: ")
            intentos = 1
            acceso_concedido = False

            # El usuario dispone de un máximo de 3 intentos
            while intentos <= 3:
                contrasena_input = input("Introduce tu contraseña: ")

                if usuario_input == identifier and contrasena_input == password:
                    print("Acceso concedido")
                    print(f"Bienvenida, {identifier}.")
                    acceso_concedido = True
                    break
                else:
                    print(f"Acceso denegado. Intento {intentos}/3")
                    intentos += 1

            # Si agotó los 3 intentos sin éxito, regresa al menú principal
            if not acceso_concedido:
                print("Demasiados intentos fallidos. Regresando al menú principal.")

    # OPCIÓN 3: SALIR DEL PROGRAMA
    elif opcion == "3":
        print("Saliendo del programa...")
        ejecutando_programa = False

    # OPCIÓN NO RECONOCIDA
    else:
        print("Opción no válida. Por favor, elige 1, 2 o 3.")
