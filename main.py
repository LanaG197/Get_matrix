def get_matrix(n, m, value):
    matrix = []  # Создаем пустой список для матрицы
    for i in range(n):  # Внешний цикл для строк матрицы
        row = []  # Создаем пустой список для строки

        for j in range(m):  # Внутренний цикл для столбцов матрицы
            row.append(value)  # Добавляем значение в строку
        matrix.append(row)  # Добавляем строку в матрицу
    return matrix  # Возвращаем матрицу


# Пример использования функции
result1 = get_matrix(3, 4, 7)

# Выводим матрицу на экран
for row in result1:
    print(row)

result2 = get_matrix(2, 6, 15)

# Выводим матрицу на экран
for row in result2:
    print(row)

result3 = get_matrix(1, 5, 20)

# Выводим матрицу на экран
for row in result3:
    print(row)
