from Ejecuciones import Ejecuciones

ejecuciones = Ejecuciones()
parametros_ingresados = []

while True:
    print("MENU")
    print("1. Ingresar parámetros")
    print("2. Imprimir parámetros ingresados")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        id = input("Ingrese el ID: ")
        nombre = input("Ingrese el nombre: ")
        contrasena = input("Ingrese la contraseña: ")
        ejecuciones.imprimir_parametros(id, nombre, contrasena)
        parametros_ingresados.append((id, nombre, contrasena))
    elif opcion == "2":
        print("Parámetros ingresados:")
        for parametros in parametros_ingresados:
            id, nombre, contrasena = parametros
            ejecuciones.imprimir_parametros(id, nombre, contrasena)
    elif opcion == "3":
        break
else:
      print("Gracias por usar el programa")