from functions import sum_digits, average, normalize_text, select_numbers

num = int(input("Введите целое число: "))
print(sum_digits(num))

nums_line = input("Введите числа через пробел: ")
nums_tokens = nums_line.split()
if not nums_tokens:
    nums_list = []
else:
    nums_list = [int(x) for x in nums_tokens]

avg_result = average(nums_list)
if avg_result is None:
    print("Нет данных")
else:
    print(avg_result)

text = input("Введите текст: ")
print(normalize_text(text))

threshold = int(input("Введите порог: "))
selected = select_numbers(nums_list, threshold)
print(selected)
