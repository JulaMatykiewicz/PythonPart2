from os import path

dir_path = path.dirname(__file__)
filename = "tekst.txt"
data_path = path.join(dir_path, filename)

lista = []
with open(data_path, "r") as f:
    for i in range(3):
        line = f.readline().strip()
        words = line.split()
        lista.extend(words)
        last_letters = [word[-1] for word in words]
        stats = {}
        for letter in last_letters:
            if letter not in stats:
                stats[letter] = 1
            else:
                stats[letter] += 1
        print(f"Liczba słów w linii {i+1}: {len(words)}")
        print("Statystyki końcówek słów:")
        for letter, count in stats.items():
            print(f"{letter}: {count} słów")

