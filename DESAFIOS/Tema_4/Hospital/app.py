# ===============================
# Clase Paciente
# ===============================
class Paciente:
    def __init__(self, nombre, sintoma, habitual):
        self.nombre = nombre
        self.sintoma = sintoma  # 1: corazón, 2: pulmón, 3: otras
        self.habitual = bool(habitual)  # True o False

    def __str__(self):
        sintomas_map = {1: "corazón", 2: "pulmón", 3: "otras"}
        return f"Paciente: {self.nombre}, Síntoma: {sintomas_map.get(self.sintoma)}, Habitual: {self.habitual}"


# ===============================
# Clase base Atención
# ===============================
class Atencion:
    def __init__(self, codigo, tipo_cobro):  
        # tipo_cobro: 1 = efectivo, 2 = tarjeta
        self.codigo = codigo
        self.tipo_cobro = tipo_cobro

    def importe_a_cobrar(self):
        """Método genérico, será redefinido por subclases"""
        return 0

    def __str__(self):
        tipo = "Efectivo" if self.tipo_cobro == 1 else "Tarjeta"
        return f"Atención código {self.codigo}, Tipo de cobro: {tipo}"


# ===============================
# Subclase Atención Médica
# ===============================
class AtencionMedica(Atencion):
    def __init__(self, codigo, tipo_cobro, paciente, importe_consulta):
        super().__init__(codigo, tipo_cobro)
        self.paciente = paciente
        self.importe_consulta = float(importe_consulta)

    def importe_a_cobrar(self):
        importe = self.importe_consulta

        # Descuento del 25% si el paciente es habitual
        if self.paciente.habitual:
            importe *= 0.75

        # Ajuste por tipo de cobro
        if self.tipo_cobro == 2:  # tarjeta
            importe *= 1.20
        else:  # efectivo
            importe *= 0.90

        return importe

    def __str__(self):
        return f"Atención Médica [{self.codigo}] - {self.paciente.nombre} - Importe consulta: {self.importe_consulta}"


# ===============================
# Subclase Atención Farmacia
# ===============================
class AtencionFarmacia(Atencion):
    def __init__(self, codigo, tipo_cobro, importe_medicamentos, cupon_descuento):
        super().__init__(codigo, tipo_cobro)
        self.importe_medicamentos = float(importe_medicamentos)
        self.cupon_descuento = max(0, float(cupon_descuento))  # el cupón no puede ser negativo

    def importe_a_cobrar(self):
        importe = self.importe_medicamentos - self.cupon_descuento
        importe = max(0, importe)  # nunca negativo

        # Ajuste por tipo de cobro
        if self.tipo_cobro == 2:  # tarjeta
            importe *= 1.30
        else:  # efectivo
            importe *= 0.95

        return importe

    def __str__(self):
        return f"Atención Farmacia [{self.codigo}] - Importe medicamentos: {self.importe_medicamentos}, Cupón: {self.cupon_descuento}"


# ===============================
# Clase Hospital
# ===============================
class Hospital:
    def __init__(self, razon_social):
        self.razon_social = razon_social
        self.atenciones = []  # colección de todas las atenciones

    def add_atencion(self, atencion):
        self.atenciones.append(atencion)

    # 1. Suma de importes de las atenciones médicas
    def importe_total_atencion_consulta(self):
        return sum(a.importe_consulta for a in self.atenciones if isinstance(a, AtencionMedica))

    # 2. Promedio de importes a cobrar dentro de un rango
    def importe_promedio_atenciones(self, minimo, maximo):
        importes = [a.importe_a_cobrar() for a in self.atenciones 
                    if isinstance(a, AtencionMedica) and minimo <= a.importe_a_cobrar() <= maximo]
        return sum(importes) / len(importes) if importes else 0

    # 3. Código de la primera atención de paciente habitual
    def codigo_primera_atencion_habitual(self):
        for a in self.atenciones:
            if isinstance(a, AtencionMedica) and a.paciente.habitual:
                return a.codigo
        return 0

    def __str__(self):
        return f"Hospital: {self.razon_social}, Atenciones registradas: {len(self.atenciones)}"


# ===============================
# Ejemplo de uso
# ===============================
if __name__ == "__main__":
    # Creamos hospital
    h = Hospital("Hospital Municipal")

    # Pacientes
    p1 = Paciente("Juan", 1, True)    # corazón, habitual
    p2 = Paciente("Ana", 2, False)    # pulmón, no habitual

    # Atenciones
    a1 = AtencionMedica(101, 1, p1, 2000)   # efectivo
    a2 = AtencionMedica(102, 2, p2, 3000)   # tarjeta
    a3 = AtencionFarmacia(201, 1, 1500, 200)  # efectivo
    a4 = AtencionFarmacia(202, 2, 5000, 0)    # tarjeta

    # Registrar en hospital
    h.add_atencion(a1)
    h.add_atencion(a2)
    h.add_atencion(a3)
    h.add_atencion(a4)

    # Mostrar resultados
    print(h)
    for a in h.atenciones:
        print(a, "-> Importe a cobrar:", a.importe_a_cobrar())

    print("\nTotal importes de consultas médicas:", h.importe_total_atencion_consulta())
    print("Promedio de importes médicos entre 1500 y 4000:", h.importe_promedio_atenciones(1500, 4000))
    print("Código primera atención habitual:", h.codigo_primera_atencion_habitual())
