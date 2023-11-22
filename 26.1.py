# Создаем и открываем файл F1 для записи
with open("F1.txt", "w") as f1:
    print("Введите данные построчно (пустая строка для завершения ввода):")

    # Ввод данных пользователем и запись их в файл F1
    while True:
        line = input()
        if not line:
            break
        f1.write(line + "\n")

# Создаем и открываем файл F2 для записи
with open("F2.txt", "w") as f2:
    # Открываем файл F1 для чтения
    with open("F1.txt", "r") as f1:
        for line in f1:
            words = line.split()
            duplicate_words = set()

            for word in words:
                if words.count(word) >= 2:
                    duplicate_words.add(word)

            # Если в строке есть хотя бы два одинаковых слова, записываем ее в файл F2
            if len(duplicate_words) >= 2:
                f2.write(line)

# Открываем файл F2 для определения номера слова с наибольшим количеством цифр
with open("F2.txt", "r") as f2:
    lines = f2.readlines()
    max_digit_count = 0
    word_number = -1

    for line in lines:
        words = line.split()

        for i, word in (words):
            digit_count = sum(c.isdigit() for c in word)

            if digit_count > max_digit_count:
                max_digit_count = digit_count
                word_number = i

    if word_number != -1:
        print(f"Номер слова с наибольшим количеством цифр: {word_number + 1}")
    else:
        print("В файле F2 нет строк с двумя одинаковыми словами.")

print("Программа завершена.")
