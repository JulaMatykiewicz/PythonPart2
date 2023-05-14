numbers = (10, -3, 4, 9, 12, -6, 0)
max_number = numbers[0]
min_number = numbers[0]

for num in numbers[1:]:
    if num > max_number:
        max_number = num
    if num < min_number:
        min_number = num

print("Największa liczba w krotce to:", max_number)
print("Najmniejsza liczba w krotce to:", min_number)
