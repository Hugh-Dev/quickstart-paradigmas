class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria con encapsulamiento.

    Atributos:
    ----------
    titular : str
        Nombre del titular de la cuenta.
    __saldo : float
        Saldo de la cuenta (atributo privado).

    Métodos:
    --------
    __init__(titular, saldo):
        Inicializa una nueva cuenta bancaria con el titular y el saldo proporcionados.
    transferir(cantidad):
        Transfiere una cantidad al saldo de la cuenta si la cantidad es positiva.
    retirar(cantidad):
        Retira una cantidad del saldo de la cuenta si hay fondos suficientes y la cantidad es válida.
    get_saldo():
        Devuelve el saldo actual de la cuenta.
    """
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def transferir(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Transferencia exitosa: ${cantidad}")
        else:
            print("Cantidad inválida.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso: ${cantidad}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def get_saldo(self):  # Método de acceso controlado
        return self.__saldo

def main():
    # Uso
    cuenta = CuentaBancaria("Ana", 1000)
    cuenta.transferir(500)
    cuenta.retirar(300)
    print(f"Saldo actual: ${cuenta.get_saldo()}")
    # No se puede acceder directamente: print(cuenta.__saldo) dará error

if __name__ == "__main__":
    main()