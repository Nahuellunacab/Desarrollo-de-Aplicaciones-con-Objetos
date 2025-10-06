from material import Material

class Libro(Material):
    def __init__(self, codigo, titulo, autor, precio_base, dias_prestados):
        super().__init__(codigo, titulo, autor, precio_base)
        self.dias_prestados = dias_prestados
        self.tipo = 1  # Tipo 1 para libros
    
    def calcular_costo_mantenimiento(self):
        periodos = self.dias_prestados // 30
        return periodos * 100