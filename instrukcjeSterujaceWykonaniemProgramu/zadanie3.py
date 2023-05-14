from random import randint

while True:
    wylosowana_liczba = randint(0, 100)
    liczba_strzalow = 0
    
    while True:
        strzal = int(input("Podaj liczbę od 0 do 100: "))
        liczba_strzalow += 1

        if strzal == wylosowana_liczba:
            print(f"Gratulacje! Odgadłeś liczbę {wylosowana_liczba} w {liczba_strzalow} strzałach.")
            break
        elif strzal < wylosowana_liczba:
            print("Liczba jest większa.")
        else:
            print("Liczba jest mniejsza.")

    odpowiedz = input("Czy chcesz zagrać jeszcze raz? (tak/nie): ")
    if odpowiedz.lower() != "tak":
        break
