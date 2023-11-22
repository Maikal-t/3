# Инициализируем переменную для суммы
total_cost = 0

# Создаем пустой словарь
w = {}

# Открываем файл для чтения
with open("F4.txt", "r") as file:
    # Читаем строки из файла
    for line in file:
        parts = line.split()
        o = parts[0]
        values = list(map(float, parts[1:4]))  # Преобразуем строки в числа
        total_subject_cost = sum(values)  # Вычисляем сумму значений
        w[o] = total_subject_cost  # Сохраняем сумму в словаре

print(w)
