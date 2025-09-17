import csv

# Definimos la clase Persona
class Persona:
    def __init__(self, documento, nombre, apellido, edad):
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.edad = int(edad)  # aseguramos que la edad sea número entero

    def __str__(self):
        return f"{self.nombre} {self.apellido} (DNI: {self.documento}, Edad: {self.edad})"


def leer_personas_csv(nombre_archivo):
    """
    Lee un archivo CSV de personas y retorna un diccionario:
    clave = documento, valor = instancia de Persona
    """
    personas = {}

    with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        next(lector)  # salteamos encabezado si lo tiene (DNI,Nombre,Apellido,Edad)

        for fila in lector:
            documento, nombre, apellido, edad = fila
            persona = Persona(documento, nombre, apellido, edad)
            personas[documento] = persona  # guardamos en el diccionario con documento como clave

    return personas


def informes(personas):
    """
    Recibe un diccionario de personas y muestra los informes solicitados.
    """
    print(f"\n📋 Cantidad de personas cargadas: {len(personas)}")

    # Personas mayores de edad
    mayores = [p for p in personas.values() if p.edad >= 18]
    print(f"👨‍🦳 Cantidad de personas mayores de edad: {len(mayores)}")

    # Apellidos que empiezan con vocal
    vocales = "AEIOUÁÉÍÓÚaeiouáéíóú"
    apellidos_vocal = [f"{p.nombre} {p.apellido}" for p in personas.values() if p.apellido[0] in vocales]
    print("\n🔤 Personas con apellido que empieza con vocal:")
    for item in apellidos_vocal:
        print(" -", item)

    # Cantidad de personas por cada apellido
    conteo_apellidos = {}
    for p in personas.values():
        conteo_apellidos[p.apellido] = conteo_apellidos.get(p.apellido, 0) + 1

    print("\n📊 Cantidad de personas por apellido:")
    for apellido, cantidad in conteo_apellidos.items():
        print(f" - {apellido}: {cantidad}")


# Programa principal
if __name__ == "__main__":
    archivo = "personas.csv"   # nombre del archivo CSV
    personas = leer_personas_csv(archivo)  # cargamos datos al diccionario
    informes(personas)         # mostramos informes
