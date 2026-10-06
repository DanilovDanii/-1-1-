# Ввод
a = int(input())
b = int(input())

# Проверка
step = 1 if a <= b else -1

# Вывод

for i in range(a, b + step, step):
    print(i)
