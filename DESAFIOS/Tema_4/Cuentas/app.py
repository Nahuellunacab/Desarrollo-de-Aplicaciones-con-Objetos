# -------------------------------------- Clase cuenta --------------------------------------------
class Cuenta:
    def __init__(self, numero, nombre, saldo):
        self.numero = numero
        self.nombre = nombre
        self.saldo = float(saldo)
    
    def __str__(self):
        return f"Cuenta [{self.numero}] - {self.nombre} - Saldo: {self.saldo}"
    
    def depositar(self, monto):
        self.saldo += float(monto)
        self.saldo = round(self.saldo, 2)
        return True
    
    def extraer(self, monto):
        # Método generico, redeninido por subclases
        raise NotImplementedError("Este método debe ser redefinido por subclases")


# -------------------------------------- Clase Caja de Ahorro --------------------------------------
class CajaAhorro(Cuenta):
    def __init__(self, numero, nombre, saldo):
        super().__init__(numero, nombre, saldo)     # Inicializando atributos de la clase base
        
    def extraer(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Saldo insuficiente")

# -------------------------------------- Clase Cuenta Corriente --------------------------------------
class CuentaCorriente(Cuenta):
    def __init__(self, numero, nombre, saldo=0, acuerdo=0):
        super().__init__(numero, nombre, saldo)
        self.acuerdo = float(acuerdo)
    
    def extraer(self, monto):
        if self.saldo - monto >= -self.acuerdo:
            self.saldo -= monto
            self.saldo = round(self.saldo, 2)
        else:
            print("Saldo insuficiente, acuerdo de descubierto excedido")

# -------------------------------------- Programa Principal --------------------------------------
if __name__ == "__main__":
    cuentas = []

    # Ejemplo de carga de cuentas
    cuentas.append(CajaAhorro(1001, "Juan Perez", 5000))
    cuentas.append(CuentaCorriente(2001, "Ana Gomez", 2000, acuerdo=1000))
    cuentas.append(CajaAhorro(1002, "Carlos Lopez", 1500))
    cuentas.append(CuentaCorriente(2002, "Laura Diaz", 3000, acuerdo=2000))

    # Operaciones de ejemplo
    cuentas[0].depositar(2000)     # Juan deposita 2000
    cuentas[1].extraer(2500)       # Ana intenta extraer 2500 (queda -500, permitido)
    cuentas[2].extraer(2000)       # Carlos intenta extraer 2000 (denegado)
    cuentas[3].extraer(4500)       # Laura extrae 4500 (queda -1500, permitido)

    # Mostrar saldos finales
    print("\n Listado de cuentas con saldos finales:")
    for c in cuentas:
        print(c)
    