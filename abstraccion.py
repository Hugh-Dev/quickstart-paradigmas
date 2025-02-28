from abc import ABC, abstractmethod

class Figura(ABC):
    """
    Clase abstracta que define la interfaz para figuras geométricas.
    Obliga a las clases hijas a implementar los métodos `area` y `perimetro`.
    """
    @abstractmethod
    def area(self):
        """
        Calcula el área de la figura.
        Debe ser implementado por las clases hijas.
        """
        pass

    @abstractmethod
    def perimetro(self):
        """
        Calcula el perímetro de la figura.
        Debe ser implementado por las clases hijas.
        """
        pass

class Circulo(Figura):
    """
    Clase que representa un círculo y calcula su área y perímetro.
    """
    def __init__(self, radio):
        """
        Inicializa un círculo con un radio dado.
        
        :param radio: Radio del círculo.
        """
        self.radio = radio

    def area(self):
        """
        Calcula el área del círculo.
        
        :return: Área del círculo.
        """
        return 3.1416 * self.radio ** 2

    def perimetro(self):
        """
        Calcula el perímetro del círculo.
        
        :return: Perímetro del círculo.
        """
        return 2 * 3.1416 * self.radio

class Rectangulo(Figura):
    """
    Clase que representa un rectángulo y calcula su área y perímetro.
    """
    def __init__(self, ancho, alto):
        """
        Inicializa un rectángulo con un ancho y alto dados.
        
        :param ancho: Ancho del rectángulo.
        :param alto: Alto del rectángulo.
        """
        self.ancho = ancho
        self.alto = alto

    def area(self):
        """
        Calcula el área del rectángulo.
        
        :return: Área del rectángulo.
        """
        return self.ancho * self.alto

    def perimetro(self):
        """
        Calcula el perímetro del rectángulo.
        
        :return: Perímetro del rectángulo.
        """
        return 2 * (self.ancho + self.alto)

def main():
    """
    Función principal que crea instancias de figuras geométricas y muestra sus áreas y perímetros.
    """
    formas = [Circulo(5), Rectangulo(4, 6)]
    for forma in formas:
        print(f"Área: {forma.area()}, Perímetro: {forma.perimetro()}")

if __name__ == "__main__":
    main()