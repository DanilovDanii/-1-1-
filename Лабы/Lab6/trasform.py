line = input("Введите числа: ")
original_list = [int(x) for x in line.split()]
new_list = [abs(x) for x in original_list]

print(original_list)
print(new_list)
