text = input("Введите текст: ")
words = text.split()
valid_words = []

for word in words:
    cleaned = word.strip(".,!?;:").lower()
    if not cleaned:
        continue
    if cleaned.endswith("й"):
        valid_words.append(cleaned)

if valid_words:
    for word in valid_words:
        print(word)
    print(len(valid_words))
else:
    print("Нет совпадений")
    print(0)
