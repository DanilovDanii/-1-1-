line = input("Введите числа: ")
tokens = line.split()

if not tokens:
    numbers = []
else:
    numbers = [int(x) for x in tokens]

filtered_list = []
for x in numbers:
    if x < 0 and x % 2 != 0:
        filtered_list.append(x)

count = len(filtered_list)
total_sum = sum(filtered_list)
sorted_copy = sorted(filtered_list)

print(filtered_list)
print(count)
print(total_sum)
print(sorted_copy)
