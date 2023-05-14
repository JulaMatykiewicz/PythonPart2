word = input("Podaj słowo: ")
word = word.strip().lower()
reversed_word = word[::-1]
if word == reversed_word:
    print("Słowo jest palindromem!")
else:
    print("Słowo nie jest palindromem.")
