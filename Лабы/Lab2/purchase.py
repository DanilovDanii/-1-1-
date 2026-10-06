# Запрос данных
price = int(input("Введите цену одной тетради (руб.): "))
count = int(input("Введите количество тетрадей: "))
paid = int(input("Введите переданную сумму (руб.): "))

# Вычисления
cost = price * count
change = paid - cost

# Вывод
print(f"стоимость {cost}, сдача {change}")
