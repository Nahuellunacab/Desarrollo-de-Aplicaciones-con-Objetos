class Ascensor:
    def __init__(self, piso_minimo, piso_maximo, capacidad):
        # Validaciones de parámetros
        if piso_minimo > piso_maximo:
            raise ValueError("El piso mínimo no puede ser mayor al piso máximo")
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser positiva")

        # El piso 0 debe estar dentro del rango
        if not (piso_minimo <= 0 <= piso_maximo):
            raise ValueError("El piso inicial 0 no está dentro del rango permitido")

        self.piso_minimo = piso_minimo
        self.piso_maximo = piso_maximo
        self.capacidad = capacidad
        self.piso_actual = 0
        self.personas = 0

    def ir_a_piso(self, piso_destino):
        """Mueve el ascensor al piso indicado si está dentro del rango"""
        if self.piso_minimo <= piso_destino <= self.piso_maximo:
            self.piso_actual = piso_destino
            return True
        return False

    def subir(self, cantidad):
        """Suben personas al ascensor"""
        if cantidad <= 0:
            return -1

        espacio_disponible = self.capacidad - self.personas
        if cantidad <= espacio_disponible:
            self.personas += cantidad
            return cantidad
        else:
            self.personas = self.capacidad
            return espacio_disponible

    def bajar(self, cantidad):
        """Bajan personas del ascensor"""
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