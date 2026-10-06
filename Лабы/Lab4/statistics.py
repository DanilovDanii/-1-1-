# Ввод
n = int(input())

# Обработка

first_num = int(input())

total_sum = first_num
positive_count = 1 if first_num > 0 else 0
max_value = first_num

for _ in range(n - 1):
    num = int(input())

    total_sum += num

    if num > 0:
        positive_count += 1

    if num > max_value:
        max_value = num

# Вывод
print(total_sum)
print(positive_count)
print(max_value)
