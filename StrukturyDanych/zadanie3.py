words = ["burak", "cukinia", "pomidor", "cytryna", "ananas", "pomidor", "dynia"]
letter = input("Podaj literę: ")
word_set = set()
for word in words:
    if word.startswith(letter):
        word_set.add(word)
print("Słowa zaczynające się na literę", letter, "to:", word_set)
