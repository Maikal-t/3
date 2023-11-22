# Инициализируем переменную для суммы
total_cost = 0
w = {}
# Открываем файл для чтения
with open("F3.txt", "r") as file:
    # Читаем строки из файла
    for line in file:
        # Разбиваем строку на части
        parts = line.split()
        if len(parts) == 2:
            product = parts[0]
            price = int(parts[1])
            # Проверяем, что цена в диапазоне от 10 до 50
            if 10 <= price <= 50:
                total_cost += price

# Выводим общую стоимость
print("Сумма стоимости товаров от 10 до 50:", total_cost)
