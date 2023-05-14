def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    return a / b

def menu():
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Wyjście")
    

    
while True:
    menu()

    wybor = input("Twój wybór: ")

    if wybor == "5":
        break

    if wybor not in ["1", "2", "3", "4"]:
        print("Nieprawidłowy wybór")
        continue

    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))

    if wybor == "1":
        wynik = dodawanie(a, b)
    elif wybor == "2":
        wynik = odejmowanie(a, b)
    elif wybor == "3":
        wynik = mnozenie(a, b)
    elif wybor == "4":
        if b == 0:
            print("Nie można dzielić przez zero")
            continue
        wynik = dzielenie(a, b)

    print("Wynik: ", wynik)

print("Koniec programu")