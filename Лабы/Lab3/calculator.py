# Запрос данных
num1 = float(input("Введите первое число: "))
operation = input("Введите операцию (+, -, *, /): ").strip()
num2 = float(input("Введите второе число: "))


# Вычисление + Вывод

if operation == "+":
    result = num1 + num2
    print(f"{result:.2f}")
elif operation == "-":
    result = num1 - num2
    print(f"{result:.2f}")
elif operation == "*":
    result = num1 * num2
    print(f"{result:.2f}")
elif operation == "/":
    if num2 == 0:
        print("Деление на ноль запрещено")
    else:
        result = num1 / num2
        print(f"{result:.2f}")
else:
    print("Неизвестная операция")
