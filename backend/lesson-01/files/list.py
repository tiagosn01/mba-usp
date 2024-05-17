numbers = [1, , 3, 4, 5]

print("List of numbers:", numbers)

print("First element:", numbers[0])  # Primeiro elemento
print("Last element:", numbers[-1])  # Último elemento

numbers.append(6)
print("List after add 6:", numbers)

numbers.remove(3)
print("List after remove 3:", numbers)

print("Elements in the list:")
for number in numbers:
    print(number)

if 2 in numbers:
    print("Number 2 exists in the list.")
else:
    print("Number 2 not exists in the list.")
