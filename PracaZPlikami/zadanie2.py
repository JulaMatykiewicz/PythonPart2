import random
from os import path

dir_path = path.dirname(__file__)
filename1 = "imiona.txt"
filename2 = "nazwiska.txt"
new_filename = "kombinacje.txt"
data_path1 = path.join(dir_path, filename1)
data_path2 = path.join(dir_path, filename2)
data_path3 = path.join(dir_path, new_filename)

if not path.exists(data_path1) or not path.exists(data_path2):
    exit()

with open(data_path1, "r", encoding="utf-8") as f:
    file_lines_names = [line.strip() for line in f.readlines()]

with open(data_path2, "r", encoding="utf-8") as f:
    file_lines_surnames = [line.strip() for line in f.readlines()]

max_amount = len(file_lines_names) * len(file_lines_surnames)

try:
    user_amount = int(input(f"Wpisz ile chcesz wygenerować kombinacji (maksymalnie {max_amount}): "))
    if user_amount > max_amount:
        print(f"Maksymalnie możesz wpisać {max_amount} kombinacji!")
        exit()
except ValueError:
    print("Wpisanie liczby nie powiodło się")
    exit()

random.shuffle(file_lines_names)
random.shuffle(file_lines_surnames)

combinations = []

for i in range(user_amount):
    name = file_lines_names[i % len(file_lines_names)]
    surname = file_lines_surnames[i % len(file_lines_surnames)]
    combination = f"{name} {surname}"
    combinations.append(combination)

with open(data_path3, "w", encoding="utf-8") as f:
    f.write("\n".join(combinations))

print("Oto twoja lista kombinacji:")
for i, combination in enumerate(combinations):
    print(f"{i+1}. {combination}")

