class repartidor:
    def __init__(self, nombre, paquete, zona):
        self.nombre = nombre
        self.paquete = paquete
        self.zona = zona

    def __str__(self):
        return f"{self.nombre} {self.paquete} {self.zona}"



def Menu():
    opcion = 0

    while opcion != 5:
        print("-_M E N U_-")
        print("1. AGREGAR REPARTIDORES")
        print("2. PAQUETES DE MAYOR A MENOR")
        print("3. RANKING")
        print("4. ESTADISTICAS")
        print("5. BUSCAR")
        print("6. SAIR")

        opcion_input = input("\nIngrese su opción: ")
        if opcion_input.isdigit():

            opcion = int(opcion_input)
            if opcion == 1:
                print()

            elif opcion == 2:
                print()

            elif opcion == 3:
                print()

            elif opcion == 4:
                print()

            elif opcion == 5:
                print()

            elif opcion == 6:
                print("gracias por usar el programa")

            else:
                print("\nOpción inválida, vuelva a intentar")
        else:
            print("\nError: ingreso de datos no numéricos")
            opcion = 0

        if opcion != 7:
            input("\nPresione ENTER para continuar...")

