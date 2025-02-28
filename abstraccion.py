from abc import ABC, abstractmethod

class Figura(ABC):  # Clase abstracta
    @abstractmethod
    def area(self):
        pass  # No implementa nada, obliga a clases hijas a definirlo

    @abstractmethod
    def perimetro(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio ** 2

    def perimetro(self):
        return 2 * 3.1416 * self.radio

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)

# Uso
formas = [Circulo(5), Rectangulo(4, 6)]
for forma in formas:
    print(f"Área: {forma.area()}, Perímetro: {forma.perimetro()}")