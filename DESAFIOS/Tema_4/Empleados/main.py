# CLASE BASE
class Empleado:
    def __init__(self, legajo, nombre, apellido, sueldo_basico):
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo_basico = float(sueldo_basico)

    def calcular_sueldo(self):
        """Método genérico, será redefinido en subclases"""
        return self.sueldo_basico

    def __str__(self):
        return f"[{self.legajo}] {self.nombre} {self.apellido}"

# CLASES DERIVADAS / SUBCLASES
class Obrero(Empleado):
    def __init__(self, legajo, nombre, apellido, sueldo_basico, dias_trabajados):
        super().__init__(legajo, nombre, apellido, sueldo_basico)
        self.dias_trabajados = int(dias_trabajados)

    def calcular_sueldo(self):
        return self.sueldo_basico * (self.dias_trabajados / 20)


class Administrativo(Empleado):
    def __init__(self, legajo, nombre, apellido, sueldo_basico, presentismo):
        super().__init__(legajo, nombre, apellido, sueldo_basico)
        self.presentismo = str(presentismo).strip().lower() in ["s", "true", "1"]

    def calcular_sueldo(self):
        return self.sueldo_basico * 1.13 if self.presentismo else self.sueldo_basico



class Vendedor(Empleado):
    def __init__(self, legajo, nombre, apellido, sueldo_basico, total_ventas):
        super().__init__(legajo, nombre, apellido, sueldo_basico)
        self.total_ventas = float(total_ventas)

    def calcular_sueldo(self):
        return self.sueldo_basico + (self.total_ventas * 0.01)
    

# LECTURA DE ARCHIVO
import csv

def leer_empleados(nombre_archivo):
    empleados = []

    with open(nombre_archivo, newline='', encoding="utf-8") as archivo:
        lector = csv.reader(archivo, delimiter=';')
        next(lector)  # saltea encabezado si lo hubiera

        for fila in lector:
            tipo, legajo, nombre, apellido, sueldo_basico, extra = fila
            if tipo == "1":
                empleados.append(Obrero(legajo, nombre, apellido, sueldo_basico, extra))
            elif tipo == "2":
                empleados.append(Administrativo(legajo, nombre, apellido, sueldo_basico, extra))
            elif tipo == "3":
                empleados.append(Vendedor(legajo, nombre, apellido, sueldo_basico, extra))

    return empleados

# INFORMES REQUERIDOS
def informes(empleados):
    # Total sueldos
    total_sueldos = sum(e.calcular_sueldo() for e in empleados)
    print(f"\n💰 Total a pagar en sueldos: {total_sueldos:.2f}")

    # Contar empleados por tipo
    cant_obreros = sum(isinstance(e, Obrero) for e in empleados)
    cant_admins = sum(isinstance(e, Administrativo) for e in empleados)
    cant_vendedores = sum(isinstance(e, Vendedor) for e in empleados)
    print(f"👷 Obreros: {cant_obreros}, 📑 Administrativos: {cant_admins}, 🛒 Vendedores: {cant_vendedores}")

    # Buscar un empleado por legajo
    legajo_buscar = input("\nIngrese un legajo a buscar: ")
    encontrado = next((e for e in empleados if e.legajo == legajo_buscar), None)
    if encontrado:
        print(f"Empleado encontrado: {encontrado} - Sueldo: {encontrado.calcular_sueldo():.2f}")
    else:
        print("⚠️ No se encontró ese legajo.")
    

# PROGRAMA PRUNCIPAL
if __name__ == "__main__":
    nombre_archivo = "c:/Users/nahue/OneDrive/Escritorio/SISTEMAS 2025/DESARROLLO DE APLICACIONES CON OBJETOS/DESAFIOS/Tema_4/Empleados/empleados.csv"
    empleados = leer_empleados(nombre_archivo)
    informes(empleados)
