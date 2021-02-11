list_of_numbers = [1, 0.5, 1 / 3]
for number in list_of_numbers:
    if number % 1 != 0:
        print(round(number, 1))
    else:
        print(number)