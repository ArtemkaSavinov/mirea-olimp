# зададим квадратную матрицу, изначально заполнив ее нулями.
# Её значения будем изменять
result = [[0] * 8 for i in range(8)]

# зададим список, хранящий числа от 0 до 63
numbers = list(range(64))

# column_number - номер столбца
# line_number - номер строки
column_number, line_number = 0, 0

# номер текущего значения, которое будем добавлять в матрицу
current_number = 0

# используем цикл while, чтобы иметь возможность изменять параметры
while column_number < 8:

    # ограничим выполнение цикла.
    # То есть, когда закончатся числа в массиве numbers,
    # и count_number примет значение 64, выполнение цикла остановится
    while line_number < 8 and current_number < 64:

        # добавим в соответствующее место матрицы текущее значение
        result[line_number][column_number] = numbers[current_number]

        # увеличим счётчик текущего значения
        current_number += 1

        # если находимся в четной колонке, то номер строки увеличивается
        if column_number in [0, 2, 4, 6]:
            line_number += 1

        # если находимся в нечетной колонке, то номер строки уменьшается
        elif column_number in [1, 3, 5, 7]:
            line_number -= 1

        # если находимся в "точке перегиба", то есть в той точке,
        # где направление меняется в противоположную сторону,
        # то изменяем значение текущей строки
        if current_number % 8 == 0:

            # если были в последней строке, то в ней же и остаемся
            if line_number == 8:
                line_number = 7

            # если были в начальной строке, то в ней же и остаемся
            else:
                line_number = 0

            # перейдем к следущему столбцу
            column_number += 1

# последовательно выведем значения матрицы так, что бы
# они занимали ровно четыре позиции
for line_number in range(8):
    for column_number in range(8):
        print("%4d" % result[line_number][column_number], end=' ')
    print()

print()


# опишем функцию поворота матрицы на 90 градусов вправо
def rotate(matrix):
    # создадим новую матрицу, заполним нулями
    newMatrix = [[0] * len(matrix) for i in range(len(matrix))]

    # расположим строки в обратном порядке
    matrix = matrix[::-1]

    # транспонируем матрицу
    for line_number in range(len(matrix)):
        for column_number in range(len(matrix)):
            newMatrix[line_number][column_number] = matrix[column_number][line_number]

    # вернем значение новой матрицы
    return newMatrix


# применим функцию поворота
result = rotate(result)

# выведем значения новой матрицы
for line_number in range(8):
    for column_number in range(8):
        print("%4d" % result[line_number][column_number], end=' ')
    print()

print()

# заново зададим матрицу для 3 схемы
result = [[0] * 8 for _ in range(8)]

# текущее значение, добавляемое в матрицу
current_number = 0

# будем заполнять матрицу по диагоналям
# len_matrix длина диагонали, которую заполняем
#  0 0 0    0 2     0 2 5
#  0 0  ->  1    -> 1 4 
#  0                3
# 

for len_matrix in range(1, 8 + 1):
    line_number, column_number = len_matrix - 1, 0

    for _ in range(len_matrix):
        # добавим текущее значение
        result[line_number][column_number] = current_number

        # увеличим текущее значение
        current_number += 1

        # сдвинемся по строке вверх, а по столбцу вправо
        line_number -= 1
        column_number += 1

# заполним вторую часть матрицы
# текущее значение
current_number = 63
# 
# 
# 
#          0           0            0            60
#        0 0 =>     0  0 =>      0 62   =>    59 62
#      0 0 0      0 0 63      0 61 63      58 61 63
# 
for len_matrix in range(1, 8):
    line_number, column_number = - len_matrix, -1
    for _ in range(len_matrix):
        result[line_number][column_number] = current_number
        current_number -= 1
        line_number += 1 # сдвигаемся по строке вниз
        column_number -= 1 # сдвигаемся по колонке влево

# зададим новую матрицу, в которую по алгоритму будем перемещать элементы из до этого
# созданной матрицы
newMatrix = [[0] * 8 for _ in range(8)]

# левая половина матрицы

# меняем местами элементы в диагоналях с чётным количеством элементов
for len_matrix in range(2, 8 + 1, 2):
    line_number, column_number = len_matrix - 1, 0
    for _ in range(len_matrix):
        newMatrix[line_number][column_number] = result[column_number][line_number]
        line_number -= 1
        column_number += 1

# элементы диагоналей с нечетным количеством элементов остаются, как есть
for len_matrix in range(1, 7 + 1, 2):
    line_number, column_number = len_matrix - 1, 0
    for _ in range(len_matrix):
        newMatrix[line_number][column_number] = result[line_number][column_number]
        line_number -= 1
        column_number += 1

# правая половина матрицы
# меняем местами элементы в диагоналях с чётным количеством элементов
for len_matrix in range(2, 8, 2):
    line_number, column_number = - len_matrix, -1
    for _ in range(len_matrix):
        newMatrix[line_number][column_number] = result[column_number][line_number]

        line_number += 1
        column_number -= 1

# элементы диагоналей с нечетным количеством элементов остаются, как есть
for len_matrix in range(1, 8, 2):
    line_number, column_number = - len_matrix, -1
    for _ in range(len_matrix):
        newMatrix[line_number][column_number] = result[line_number][column_number]

        line_number += 1
        column_number -= 1

# вывод матрицы
for line_number in range(len(newMatrix)):
    for column_number in range(len(newMatrix)):
        print("%4d" % newMatrix[line_number][column_number], end=' ')
    print()

