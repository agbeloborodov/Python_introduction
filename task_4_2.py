''' Задача 4_2.    Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
и считает среднее арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)'''

from random import randint

def create_random_matrix(rows_num = 10, columns_num = 10, lower_limit = -100, upper_limit = 100):     # Функция задания матрицы (row x column)  из случайных чисел
    created_list = [[randint(lower_limit, upper_limit) for j in range(columns_num)] for i in range(rows_num)]
    return created_list

def print_random_matrix(any_matrix):        # Функция вывода матрицы в консоль
    for row in any_matrix:
        for item in row:
            print(f'{item:7}', end = '')
        print()

number_rows = int(input('Введите количество строк: '))
number_columns = int(input('Введите количество столбцов: '))
random_matrix = create_random_matrix(number_rows, number_columns)
print('Сгенерирована вот такая матрица: ')
print_random_matrix(random_matrix)
for item in range(number_rows):
    arith_mean = 0
    for jtem in range(number_columns):
        arith_mean += random_matrix[item][jtem]
    print(f'Среднее арифметическое элементов {item + 1}-й строки = {round(arith_mean / number_columns, 3)}')