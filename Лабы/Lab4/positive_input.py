# счетчик
rejected_attempts = 0

# Бесконечный цикл. т.к. удобно
while True:
    num = int(input())

    if num > 0:
        break

    rejected_attempts += 1

square = num ** 2

# Вывод

print(square)
print(rejected_attempts)
