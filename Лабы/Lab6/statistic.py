line = input("Введите числа: ")
tokens = line.split()

if not tokens:
    print("Нет данных")
else:
    numbers = [int(x) for x in tokens]

    total_count = len(numbers)
    total_sum = sum(numbers)
    min_val = min(numbers)
    max_val = max(numbers)
    average = total_sum / total_count

    print(total_count)
    print(total_sum)
    print(min_val)
    print(max_val)
    print(f"{average:.2f}")
