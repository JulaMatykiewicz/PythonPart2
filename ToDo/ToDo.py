import json
import atexit

class Zadanie:
    def __init__(self, id, tytul, opis, termin_wykonania):
        self._id = id
        self._tytul = tytul
        self._opis = opis
        self._termin_wykonania = termin_wykonania
    
    def __str__(self):
        return f"ID: {self._id}, Tytuł: {self._tytul}, Termin: {self._termin_wykonania}"
    
    def get_id(self):
        return self._id
    
    def get_tytul(self):
        return self._tytul
    
    def get_opis(self):
        return self._opis
    
    def get_termin_wykonania(self):
        return self._termin_wykonania

class ZarzadzanieZadaniami:
    def __init__(self):
        self._zadania = []
        atexit.register(self.zapisz_zadania)  # Rejestracja funkcji zapisującej zadania przy wyjściu z programu
    
    def dodaj_zadanie(self):
        id = input("Podaj ID zadania: ")
        if self.zadanie_istnieje(id):
            print("Zadanie o podanym ID już istnieje.")
            return
        
        tytul = input("Podaj tytuł zadania: ")
        opis = input("Podaj opis zadania: ")
        termin = input("Podaj termin wykonania zadania: ")
        
        zadanie = Zadanie(id, tytul, opis, termin)
        self._zadania.append(zadanie)
        print("Zadanie zostało dodane.")
    
    def zadanie_istnieje(self, id):
        for zadanie in self._zadania:
            if zadanie.get_id() == id:
                return True
        return False
    
    def usun_zadanie(self):
        id = input("Podaj ID zadania do usunięcia: ")
        znalezione = False
        for zadanie in self._zadania:
            if zadanie.get_id() == id:
                self._zadania.remove(zadanie)
                print("Zadanie zostało usunięte.")
                znalezione = True
                break
        if not znalezione:
            print("Zadanie o podanym ID nie zostało znalezione.")
    
    def aktualizuj_zadanie(self):
        id = input("Podaj ID zadania do aktualizacji: ")
        znalezione = False
        for zadanie in self._zadania:
            if zadanie.get_id() == id:
                tytul = input("Podaj nowy tytuł zadania: ")
                opis = input("Podaj nowy opis zadania: ")
                termin = input("Podaj nowy termin wykonania zadania: ")
                
                zadanie._tytul = tytul
                zadanie._opis = opis
                zadanie._termin_wykonania = termin
                
                print("Zadanie zostało zaktualizowane.")
                znalezione = True
                break
        if not znalezione:
            print("Zadanie o podanym ID nie zostało znalezione.")
    
    def wyswietl_zadania(self):
        if len(self._zadania) > 0:
            for zadanie in self._zadania:
                print(f"ID: {zadanie.get_id()}, Tytuł: {zadanie.get_tytul()}, Termin: {zadanie.get_termin_wykonania()}")
                opis = input("Czy chcesz wyświetlić opis zadania? (Tak/Nie): ")
                if opis.lower() == "tak":
                    print(f"Opis zadania: {zadanie.get_opis()}")
                print()
        else:
            print("Brak zapisanych zadań.")
    
    def zapisz_zadania(self):
        with open("zadania.json", "w") as file:
            zadania_json = []
            for zadanie in self._zadania:
                zadanie_json = {
                    "id": zadanie.get_id(),
                    "tytul": zadanie.get_tytul(),
                    "opis": zadanie.get_opis(),
                    "termin": zadanie.get_termin_wykonania()
                }
                zadania_json.append(zadanie_json)
            json.dump(zadania_json, file)
    
    def odczytaj_zadania(self):
        try:
            with open("zadania.json", "r") as file:
                zadania_json = json.load(file)
                for zadanie_json in zadania_json:
                    zadanie = Zadanie(zadanie_json["id"], zadanie_json["tytul"], zadanie_json["opis"], zadanie_json["termin"])
                    self._zadania.append(zadanie)
        except FileNotFoundError:
            print("Brak zapisanych zadań.")
    
    def uruchom(self):
        self.odczytaj_zadania()
        self.wyswietl_zadania()  # Wyświetlenie zapisanych zadań przy uruchomieniu
        
        while True:
            print("1. Dodaj zadanie")
            print("2. Usuń zadanie")
            print("3. Aktualizuj zadanie")
            print("4. Wyświetl zadania")
            print("5. Zapisz zadania")
            print("6. Wyjście")
            
            wybor = input("Wybierz opcję: ")
            
            if wybor == "1":
                self.dodaj_zadanie()
            elif wybor == "2":
                self.usun_zadanie()
            elif wybor == "3":
                self.aktualizuj_zadanie()
            elif wybor == "4":
                self.wyswietl_zadania()
            elif wybor == "5":
                self.zapisz_zadania()  # Zapisanie zadań
                print("Zadania zostały zapisane.")
            elif wybor == "6":
                break
            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")

zarzadzanie = ZarzadzanieZadaniami()
zarzadzanie.uruchom()

