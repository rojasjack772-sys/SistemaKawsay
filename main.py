from cita import registrar_cita, mostrar_citas, buscar_codigo_cita, registrar_medico

while True:
        print("\n=== MENÚ DE OPCIONES ===")
        print("1. Registrar Cita")
        print("2. Registrar Medico")
        print("3. Datos de cita")
        print("4. Buscar cita por código")
        print("5. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            registrar_cita()
        elif opcion == "2":
            registrar_medico()
        elif opcion == "3":
            mostrar_citas()
        elif opcion == "4":
            cod = input("Ingrese el código de la cita a buscar (ej. 001): ")
            print(buscar_codigo_cita(cod))
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")