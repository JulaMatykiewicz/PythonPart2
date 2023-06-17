import json
from datetime import datetime, timedelta
import os


class Task:
    def __init__(self, zadanieID, tytul, opis, data):
        self.zadanieID = zadanieID
        self.tytul = tytul
        self.opis = opis
        self.data = data


class TaskManager:
    """Klasa do zarządzania zadaniami."""
    _highest_id = 0

    def __init__(self):
        self.tasks = []

    def ClearTask(self):
        """Usuwa wszystkie zadania."""
        self.tasks.clear()

    def dodajZadanie(self, tytul, opis, data):
        zadanieID = TaskManager.get_highest_id() + 1
        while self.get_task(zadanieID) is not None:
            zadanieID += 1
        TaskManager.set_highest_id(zadanieID)
        task = Task(zadanieID, tytul, opis, data)
        self.tasks.append(task)
        print("Dodano nowe zadanie, ID:", zadanieID)

    def delete_task(self, zadanieID):
        found_task = False
        for task in self.tasks:
            if task.zadanieID == zadanieID:
                self.tasks.remove(task)
                found_task = True
                break
        if found_task:
            print("Usunięto zadanie o ID:", zadanieID)
        else:
            print("Nie znaleziono zadania o takim ID.")

    def aktualizuj(self, zadanieID, tytul, opis, data):
        for task in self.tasks:
            if task.zadanieID == zadanieID:
                task.tytul = tytul
                task.opis = opis
                task.data = data
                print("Zaktualizowano zadanie o ID:", zadanieID)
                return
        print("Nie znaleziono zadania o takim ID.")

    def get_task(self, zadanieID):
        for task in self.tasks:
            if task.zadanieID == zadanieID:
                return task
        return None

    def get_all_tasks(self):
        if not self.tasks:
            print("Brak zapisanych zadań.")
        else:
            for task in self.tasks:
                print("ID:", task.zadanieID)
                print("Tytuł:", task.tytul)
                print("Termin wykonania:", task.data.strftime("%d-%m-%Y"))
                print("Opis:", task.opis)

    def zapiszZadaniePlik(self, file_path):
        tasks_data = []
        for task in self.tasks:
            task_data = {
                "ID": task.zadanieID,
                "Tytuł zadania": task.tytul,
                "Opis zadania": task.opis,
                "Data": task.data.strftime("%d-%m-%Y")
            }
            tasks_data.append(task_data)

        with open(file_path, "w") as file:
            json.dump(tasks_data, file, indent=4)

    def OdczytZPliku(self, file_path):
        if not os.path.exists(file_path):
            print("Nie znaleziono pliku z zapisanymi zadaniami.")
            return

        try:
            with open(file_path, "r") as file:
                tasks_data = json.load(file)

            # Usuń wszystkie zadania przed wczytaniem nowych danych
            self.ClearTask()

            for task_data in tasks_data:
                zadanieID = task_data["ID"]
                tytul = task_data["Tytuł zadania"]
                opis = task_data["Opis zadania"]
                data_str = task_data["Data"]
                data = datetime.strptime(data_str, "%d-%m-%Y")
                task = Task(zadanieID, tytul, opis, data)
                self.tasks.append(task)

            print("Wczytano zadania z pliku:", file_path)

        except Exception as e:
            print("Wystąpił błąd podczas odczytu pliku:", str(e))

    @classmethod #Dodanie enkapsulacji
    def get_highest_id(cls):
        return cls._highest_id

    @classmethod#Enkapsulacja
    def set_highest_id(cls, value):
        cls._highest_id = value


#MENU

def display_menu():
    print("                        ")
    print("     ToDo LISTA")
    print("---------------------")
    print("1. Dodaj nowe zadanie")
    print("2. Wyświetl zadanie")
    print("3. Usuń zadanie")
    print("4. Zaktualizuj zadanie")
    print("5. Zapisz zadania do pliku")
    print("6. Wczytaj zadania z pliku")
    print("7. Wyświetl wszystkie zadania")
    print("8. Wyjście")


def validate_datetime(date_str):  # Sprawdza poprawnosc wpisania daty
    try:
        return datetime.strptime(date_str, "%d-%m-%Y").date()
    except ValueError:
        print("Niepoprawny format daty. Wprowadź datę w formacie DD-MM-RRRR.")
        return None


def main():
    task_manager = TaskManager()
    file_path = os.path.join(os.path.dirname(__file__), "Zapis", "Autozapis.json")
    task_manager.OdczytZPliku(file_path)
    task_manager.get_all_tasks()
    while True:
        display_menu()
        choice = input("Wybierz opcję: ")
        if choice == "1":
            tytul = input("Podaj tytuł zadania: ")
            opis = input("Podaj opis zadania: ")
            data_str = input("Podaj termin wykonania zadania w formacie DD-MM-RRRR: ")
            data = validate_datetime(data_str)
            if data is not None:
                task_manager.dodajZadanie(tytul, opis, data)
        elif choice == "2":
            try:
                zadanieID = int(input("Podaj ID zadania do wyświetlenia: "))
                task = task_manager.get_task(zadanieID)
                if task:
                    print("ID:", task.zadanieID)
                    print("Tytuł zadania:", task.tytul)
                    print("Termin wykonania zadania:", task.data)
                    show_details = input("Czy wyświetlić opis zadania? Wpisz 'tak' lub 'nie': ")
                    if show_details == "tak":
                        print("Opis:", task.opis)
                else:
                    print("Brak podanego ID")
            except ValueError:
                print("Nieprawidłowy format ID. Podaj liczbę całkowitą jako ID zadania.")

        elif choice == "3":
            try:
                zadanieID = int(input("Podaj ID zadania do usunięcia: "))
                task = task_manager.get_task(zadanieID)
                if task:
                    usuwanie = input(
                        "Czy na pewno chcesz usunąć to zadanie? Wpisz 'tak' lub 'nie': ")
                    if usuwanie == "tak":
                        task_manager.delete_task(zadanieID)
                    elif usuwanie == "nie":
                        continue
                    else:
                        print(
                            "Musisz podać odpowiedź 'tak', jeżeli chcesz usunąć zadanie lub 'nie', jeżeli chcesz wyjść do ekranu głównego!")
                else:
                    print("Brak podanego ID.")
            except ValueError:
                print("Nieprawidłowy format ID. Podaj liczbę całkowitą jako ID zadania.")

        elif choice == "4":
            try:
                zadanieID = int(input("Podaj ID zadania do zaktualizowania: "))
                task = task_manager.get_task(zadanieID)
                if task:
                    tytul = input("Podaj nowy tytuł zadania: ")
                    opis = input("Podaj nowy opis zadania: ")
                    data_str = input("Podaj nowy termin wykonania (DD-MM-RRRR): ")
                    data = validate_datetime(data_str)
                    if data is not None:
                        task_manager.aktualizuj(zadanieID, tytul, opis, data)
                else:
                    print("Brak podanego ID")
            except ValueError:
                print("Nieprawidłowy format ID. Podaj liczbę całkowitą jako ID zadania.")
        elif choice == "5":
            filename = input("Podaj nazwę pliku do zapisu: ")
            file_path = os.path.join(os.path.dirname(
                __file__), "Zapis", filename)
            task_manager.zapiszZadaniePlik(file_path)
            print("Zapisano zadania do pliku.")
        elif choice == "6":
            filename = input("Podaj nazwę pliku do wczytania: ")
            file_path = os.path.join(os.path.dirname(__file__), "Zapis", filename)
            task_manager.OdczytZPliku(file_path)
            task_manager.get_all_tasks()

        elif choice == "7":
            task_manager.get_all_tasks()
        elif choice == "8":
            file_path = os.path.join(
                os.path.dirname(__file__), "Zapis", "Autozapis.json")
            task_manager.zapiszZadaniePlik(file_path)
            print("Program zakończył swoje działanie.")
            break
        else:
            print("Nieprawidłowa opcja. Wybierz ponownie.")


if __name__ == "__main__":
    main()
