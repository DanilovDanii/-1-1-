line = input("Введите числа: ")
tokens = line.split()

if not tokens:
    print("Нет данных")
else:
    numbers = [int(x) for x in tokens]
    max_val = max(numbers)

    indices = [i for i, x in enumerate(numbers) if x == max_val]
    print(indices)
