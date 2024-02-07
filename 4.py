# опишем рекурсивную функцию для решения задачи
# когда достигаем края, то возвращем значение ячейки
def task(n, m, matrix):
    if n > 1:
        if m > 1:
            (dv, dp), (rv, rp) = task(n - 1, m, matrix), task(n, m - 1, matrix)
        else:
            (dv, dp), (rv, rp) = task(n - 1, m, matrix), (0, "")
    else:
        return matrix[-n][-m] + 0, ""

    # сравнение результатов
    if dv > rv:
        return matrix[-n][-m] + dv, "D " + dp
    else:
        return matrix[-n][-m] + rv, "R " + rp

# ввод первых двух чисел
n, m = [int(x) for x in input().split()]

# ввод матрицы
matrix = []
for _ in range(n):
    matrix.append([int(element) for element in input().split()])

result = task(n, m, matrix)

print(result[0]) # максимальная сумма
print(result[1]) # последовательность