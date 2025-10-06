class Material:
    def __init__(self, codigo, titulo, autor, precio_base):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.precio_base = precio_base
    
    def calcular_costo_mantenimiento(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")