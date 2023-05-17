class Czytelnik:
    def __init__(self, imie, nazwisko, karta, nr_telefonu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.__karta = karta
        self.nr_telefonu = nr_telefonu
    
    def __str__(self):
        return f"{self.imie} {self.nazwisko} - Numer karty: {self.__karta}, nr telefonu: {self.nr_telefonu}"
    
czytelnik1 = Czytelnik("Jan", "Kowalski", "12345678901", "123456789")
czytelnik2 = Czytelnik("Anna", "Nowak", "98765432101", "987654321")

print(czytelnik1)
print(czytelnik2)

def pobierz_numer(self):
    return self.__karta

print(pobierz_numer(czytelnik1))