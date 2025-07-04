class CuentaBancaria:
    def __init__(self, titular, saldo:float ):
        self.titular = titular
        self.saldo = saldo

    def depositar(self,cantidad):
        self.saldo += cantidad


    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            print("Hay suficiente dinero")
            self.saldo -= cantidad

        else: 
            print("fondos insuficientes")    


    def mostrar_saldo(self):    
        print(f"Su saldo actual es {self.saldo}")




cuenta = CuentaBancaria("Santiago", 1000) 
cuenta.mostrar_saldo()
cuenta.depositar(500)
cuenta.mostrar_saldo()
cuenta.retirar(300)
cuenta.mostrar_saldo()
cuenta.retirar(1500)     
