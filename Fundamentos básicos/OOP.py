# CLASE

class CuentaBancaria:

    def __init__(self, num_cuenta, nombre_titular, balance):
        self.num_cuenta = num_cuenta
        self.nombre_titular = nombre_titular
        self.balance = balance

# FUNCIONALIDAD

    def generar_balance(self):
        print(self.balance)

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto

# INSTANCIA

mi_cuenta = CuentaBancaria("105-356-643", "Will Smith", 1000000)

print(str("Titular:"), mi_cuenta.nombre_titular)
print(str("Balance:"), mi_cuenta.balance, str("USD"))

mi_cuenta.generar_balance()
mi_cuenta.depositar(50000)
mi_cuenta.generar_balance()
