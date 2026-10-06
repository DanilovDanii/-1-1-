# Программа расчёта заказа для магазина животных (без условий, циклов и коллекций)

# 1. Запрос общих данных о заказе

# region

order_title = input("Введите название заказа: ")
customer_name = input("Введите имя заказчика: ")

pos1_name = input("Введите название первой позиции: ")
pos1_count = int(input("Введите количество для первой позиции: "))
pos1_price = float(input("Введите цену за единицу первой позиции (в рублях): "))

pos2_name = input("Введите название второй позиции: ")
pos2_count = int(input("Введите количество для второй позиции: "))
pos2_price = float(input("Введите цену за единицу второй позиции (в рублях): "))

delivery_cost = float(input("Введите стоимость доставки (в рублях): "))
amount_paid = float(input("Введите внесённую сумму (в рублях): "))

# endregion

# 2. Расчёты

# region

pos1_total = pos1_count * pos1_price
pos2_total = pos2_count * pos2_price

items_total_no_delivery = pos1_total + pos2_total
grand_total_with_delivery = items_total_no_delivery + delivery_cost
total_items_count = pos1_count + pos2_count
change = amount_paid - grand_total_with_delivery

# endregion

# 3. Вывод результатов

# region

print("\n" + "="*40)
print(f"Заказ: {order_title}")
print(f"Заказчик: {customer_name}")
print("-"*40)
print(f"{pos1_name} | {pos1_count} | {pos1_price:.2f} | {pos1_total:.2f}")
print(f"{pos2_name} | {pos2_count} | {pos2_price:.2f} | {pos2_total:.2f}")
print("-"*40)
print(f"Стоимость товаров без доставки: {items_total_no_delivery:.2f} руб.")
print(f"Стоимость доставки: {delivery_cost:.2f} руб.")
print(f"Общая сумма к оплате: {grand_total_with_delivery:.2f} руб.")
print(f"Общее количество единиц товаров: {total_items_count}")
print(f"Внесено: {amount_paid:.2f} руб.")
print(f"Сдача: {change:.2f} руб.")
print("="*40)

# endregion
