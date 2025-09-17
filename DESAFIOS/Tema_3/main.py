class Persona:
    # Constructor de la clase Persona, inicializa los atributos documento, nombre, apellido y edad
    def __init__(self, documento, nombre, apellido, edad):
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    # Método especial para mostrar la información de la persona como string
    def __str__(self):
        return f"Documento: {self.documento}, Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}"

def main():
    personas = []  # Lista para almacenar los objetos Persona

    # Solicita al usuario la cantidad de personas a cargar
    n = int(input("Ingrese la cantidad de personas a cargar: "))

    # Bucle para cargar los datos de cada persona
    for i in range(n):
        print(f"\nPersona {i+1}:")
        documento = input("Ingrese el documento: ")  # Solicita el documento
        nombre = input("Ingrese el nombre: ")        # Solicita el nombre
        apellido = input("Ingrese el apellido: ")    # Solicita el apellido
        edad = int(input("Ingrese la edad: "))       # Solicita la edad y la convierte a entero

        persona = Persona(documento, nombre, apellido, edad)  # Crea un objeto Persona con los datos ingresados
        personas.append(persona)  # Agrega la persona a la lista

    print("\nPersonas cargadas:")
    # Muestra la información de todas las personas cargadas
    for persona in personas:
        print(persona)
    
    # Busca la persona con menor edad en la lista
    menor = min(personas, key=lambda x: x.edad)
    print("La persona menor de edad es:")
    print(menor)  # Muestra la persona menor de edad

# Punto de entrada del programa, ejecuta la función main si el archivo se ejecuta directamente
if __name__ == "__main__":
    main()
