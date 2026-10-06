# Запрос данных
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

# Обработка
if a <= b and a <= c:
    minimum = a
elif b <= c:
    minimum = b
else:
    minimum = c

# Вывод
print(f"Минимальное число: {minimum}")
