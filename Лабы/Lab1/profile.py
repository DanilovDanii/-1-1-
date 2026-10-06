# Запрос данных

# region

last_name = input("Введите фамилию: ")
first_name = input("Введите имя: ")
group = input("Введите группу: ")
city = input("Введите город: ")
age = int(input("Введите возраст (полных лет): "))
favorite_subject = input("Введите любимый предмет: ")
hours_per_week = float(input("Введите количество часов подготовки в неделю: "))

# endregion

# Обработка

# region

full_name = f"{first_name} {last_name}"
age_in_4_years = age + 4
hours_in_4_weeks = hours_per_week * 4
hours_per_day = hours_per_week / 7

# endregion

# Вывод, хз че тут обьяснять

# region
print("\n" + "="*30)
print("       КАРТОЧКА СТУДЕНТА       ")
print("="*30)
print(f"Студент: {full_name}")
print(f"Группа: {group}")
print(f"Город: {city}")
print(f"Возраст через 4 года: {age_in_4_years} лет")
print(f"Подготовка за неделю: {hours_per_week:.2f} ч.")
print(f"Подготовка за 4 недели: {hours_in_4_weeks:.2f} ч.")
print(f"Среднее время в день: {hours_per_day:.2f} ч.")
print("="*30)

# endregion
