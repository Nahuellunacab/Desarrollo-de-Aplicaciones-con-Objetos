# -------------------------------------- Clase Ascensor --------------------------------------------
class Ascensor:
    def __init__(self, capacidad, piso_minimo, piso_maximo):
        self.capacidad = capacidad
        self.piso_minimo = piso_minimo
        self.piso_maximo = piso_maximo
        self.piso_actual = 0
        self.personas = 0

    def ir_a_piso(self, piso_destino):
        if self.piso_minimo <= piso_destino <= self.piso_maximo:
            self.piso_actual = piso_destino
            return True
        else:
            return False

    def subir_personas(self, cantidad):
        if cantidad <= 0:
            return -1
        espacio_disponible = self.capacidad - self.personas
        if cantidad <= espacio_disponible:
            self.personas += cantidad
            return cantidad
        else:
            self.personas = self.capacidad
            return espacio_disponible

    def bajar_personas(self, cantidad):
        if cantidad <= 0:
            return -1
        if cantidad <= self.personas:
            self.personas -= cantidad
            return cantidad
        else:
            cantidad_bajada = self.personas
            self.personas = 0
            return cantidad_bajada

    def __str__(self):
        return f"Ascensor en piso {self.piso_actual} con {self.personas} personas"


# -------------------------------------- Menú interactivo --------------------------------------------
def menu():
    # Creamos un ascensor con capacidad de 5 personas, entre pisos -2 y 10
    asc = Ascensor(5, -2, 10)

    while True:
        print("\n--- Menú Ascensor ---")
        print("1. Ir a un piso")
        print("2. Subir personas")
        print("3. Bajar personas")
        print("4. Mostrar estado")
        print("5. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            piso = int(input("Ingrese el piso destino: "))
            if asc.ir_a_piso(piso):
                print(f"Ascensor se movió al piso {piso}")
            else:
                print("Piso fuera de rango permitido.")

        elif opcion == "2":
            cant = int(input("Ingrese la cantidad de personas que suben: "))
            resultado = asc.subir_personas(cant)
            if resultado == -1:
                print("Cantidad inválida.")
            else:
                print(f"Subieron {resultado} personas.")

        elif opcion == "3":
            cant = int(input("Ingrese la cantidad de personas que bajan: "))
            resultado = asc.bajar_personas(cant)
            if resultado == -1:
                print("Cantidad inválida.")
            else:
                print(f"Bajaron {resultado} personas.")

        elif opcion == "4":
            print(asc)

        elif opcion == "5":
            print("Fin de la simulación.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


# -------------------------------------- Programa principal --------------------------------------------
if __name__ == "__main__":
    menu()
