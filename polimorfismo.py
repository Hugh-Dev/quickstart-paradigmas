class Ave:
    """
    Clase base que representa a un ave.
    """
    def volar(self):
        """
        Método que indica si el ave puede volar.
        """
        return "Esta ave puede volar."

class Aguila(Ave):
    """
    Clase que representa a un águila, hereda de Ave.
    """
    def volar(self):
        """
        Método que indica cómo vuela el águila.
        """
        return "El águila vuela alto y rápido."

class Pinguino(Ave):
    """
    Clase que representa a un pingüino, hereda de Ave.
    """
    def volar(self):
        """
        Método que indica que el pingüino no puede volar.
        """
        return "Los pingüinos no pueden volar, nadan en el agua."

def main():
    """
    Función principal que crea una lista de aves y muestra cómo vuelan.
    """
    aves = [Aguila(), Pinguino(), Ave()]
    for ave in aves:
        print(ave.volar())  # Cada clase responde de forma distinta

if __name__ == "__main__":
    main()