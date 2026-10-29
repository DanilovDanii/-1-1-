from functions import average, normalize_text, sum_digits, select_numbers

assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""

test_list = [-5, 0, 2, 5]
original_copy = list(test_list)
assert select_numbers(test_list, 2) == [-5]
assert test_list == original_copy

assert select_numbers([], 2) == []
assert select_numbers([-5, -5, 0, 2], 2) == [-5, -5]
assert select_numbers([1, 2, 3], 2) == [1]

print("Базовые проверки пройдены")
