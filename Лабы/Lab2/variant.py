# Ввод данных для Варианта 14: Плитки и упаковки
total = int(input("Введите общее количество плиток: "))
capacity = int(input("Введите вместимость одной упаковки: "))

# Расчеты без использования циклов и условий
full_units = total // capacity
remainder = total % capacity

# Формула нахождения минимального числа упаковок для всего объема плиток.
# Для total = 0 сработает корректно (0 + capacity - 1) // capacity == 0, 
# так как capacity >= 1.
# Логическое выражение (total > 0) в Python возвращает True (1) или False (0), 
# что позволяет обнулить результат при total = 0 без использования if.
has_elements = int(total > 0)
total_units = ((total + capacity - 1) // capacity) * has_elements

# Вывод результатов
print(f"Полных {full_units}, остаток {remainder}, всего {total_units}")
