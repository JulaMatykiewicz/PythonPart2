import json

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    if len(tasks) == 0:
        print("Brak zapisanych zadań.")
    else:
        for task in tasks:
            print("ID:", task["id"])
            print("Tytuł:", task["title"])
            print("Termin wykonania:", task["due_date"])
            print()

def add_task(tasks):
    title = input("Podaj tytuł zadania: ")
    description = input("Podaj opis zadania: ")
    due_date = input("Podaj termin wykonania zadania: ")
    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "due_date": due_date
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print("Zadanie zostało dodane.")

def delete_task(tasks):
    task_id = int(input("Podaj ID zadania do usunięcia: "))
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Zadanie zostało usunięte.")
            return
    print("Nie znaleziono zadania o podanym ID.")

def update_task(tasks):
    task_id = int(input("Podaj ID zadania do aktualizacji: "))
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = input("Podaj nowy tytuł zadania: ")
            task["description"] = input("Podaj nowy opis zadania: ")
            task["due_date"] = input("Podaj nowy termin wykonania zadania: ")
            save_tasks(tasks)
            print("Zadanie zostało zaktualizowane.")
            return
    print("Nie znaleziono zadania o podanym ID.")

def main():
    tasks = load_tasks()
    print("Lista zadań:")
    display_tasks(tasks)
    while True:
        print("Wybierz opcję:")
        print("1. Dodaj zadanie")
        print("2. Usuń zadanie")
        print("3. Aktualizuj zadanie")
        print("4. Zapisz zadania do pliku")
        print("0. Wyjdź z programu")
        choice = input("Twój wybór: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            delete_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
        elif choice == "0":
            break
        else:
            print("Nieprawidłowa opcja. Wybierz ponownie.")

if __name__ == "__main__": #to mi potrzebne, bez tego nie pojawialy sie taski przy ponownym uruchomieniu
    main()