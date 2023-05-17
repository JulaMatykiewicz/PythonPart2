import random

def load_data(filename):
    with open(filename, 'r') as file:
        data = file.read().splitlines()
    return data

def generate_combinations(names, surnames, num_combinations):
    combinations = []
    while len(combinations) < num_combinations:
        name = random.choice(names)
        surname = random.choice(surnames)
        combination = f"{name} {surname}"
        if combination not in combinations:
            combinations.append(combination)
    return combinations

def save_combinations(combinations, filename):
    with open(filename, 'w') as file:
        for combination in combinations:
            file.write(combination + '\n')
    print(f"Zapisano {len(combinations)} kombinacji do pliku {filename}.")

# Wczytanie danych z plików
names = ('imiona.txt')
surnames = ('nazwiska.txt')

# Pobranie liczby kombinacji od użytkownika
num_combinations = int(input("Podaj liczbę kombinacji do wygenerowania: "))

# Generowanie i zapisywanie kombinacji
combinations = generate_combinations(names, surnames, num_combinations)
save_combinations(combinations, 'kombinacje.txt')

