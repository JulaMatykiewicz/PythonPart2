from abc import ABC, abstractmethod

class Ksztalt(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def oblicz_pole(self):
        pass
    
    @abstractmethod
    def oblicz_obwod(self):
        pass

class Prostokat(Ksztalt):
    def __init__(self, dlugosc, szerokosc):
        super().__init__()
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc
    
    def oblicz_pole(self):
        return self.dlugosc * self.szerokosc
    
    def oblicz_obwod(self):
        return 2 * (self.dlugosc + self.szerokosc)

class Kolo(Ksztalt):
    def __init__(self, promien):
        super().__init__()
        self.promien = promien
    
    def oblicz_pole(self):
        return 3.14 * self.promien**2
    
    def oblicz_obwod(self):
        return 2 * 3.14 * self.promien

# Tworzenie obiektów i wywoływanie metod
prostokat = Prostokat(4, 6)
kolo = Kolo(5)

print("Prostokąt:")
print("Pole:", prostokat.oblicz_pole())
print("Obwód:", prostokat.oblicz_obwod())

print("Koło:")
print("Pole:", kolo.oblicz_pole())
print("Obwód:", kolo.oblicz_obwod())

