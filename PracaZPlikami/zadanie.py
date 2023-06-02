from os import path

dir_path = path.dirname(__file__)
filename = "tekst.txt"
data_path = path.join(dir_path, filename)

lista = []
word_count = 0
last_letters_stats = {}

import string
from os import path
dir_path = path.dirname(__file__)
filename = "tekst.txt"
data_path = path.join(dir_path, filename)

lista = []
word_count = 0
last_letters_stats = {}

with open(data_path, "r") as f:
    for i in range(3):
        line = f.readline().strip()
        words = line.split()
        lista.extend(words)
        for word in words:
            while len(word) > 0 and word[-1] in string.punctuation:
                word = word[:-1]
            if word:
                word_count += 1
                last_letter = word[-1]
                if last_letter not in last_letters_stats:
                    last_letters_stats[last_letter] = 1
                else:
                    last_letters_stats[last_letter] += 1

print(f"Liczba słów we wszystkich liniach: {word_count}")
print("Statystyki końcówek słów:")
for letter, count in last_letters_stats.items():
    print(f"{letter}: {count} słów")
