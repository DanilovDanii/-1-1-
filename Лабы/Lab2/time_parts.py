# Запрос данных
total_seconds = int(input("Введите количество секунд: "))

# Вычисления
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

# Вывод
print(f"{hours} ч {minutes} мин {seconds} с")
