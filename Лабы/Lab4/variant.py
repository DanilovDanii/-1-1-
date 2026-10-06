# Ввод
n = int(input())

# Обработка

count_selected = 0
total_sum = 0


for _ in range(n):
    num = int(input())

    if num % 5 == 0:
        count_selected += 1
        total_sum += num

# Вывод результатов
print(count_selected)
print(total_sum)
