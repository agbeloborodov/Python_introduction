''' Задача 4_1.    Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12'''

import random

def create_random_list(lenght = 10, lower_limit = -100, upper_limit = 100):     # Функция задания списка из случайных чисел
    created_list = []
    for item in range (lenght):
        random.randint(lower_limit, upper_limit)
        created_list.append(random.randint(lower_limit, upper_limit))
    return created_list

inspectable_list = create_random_list(11)
print(f'Пусть мы имеем такой список:  {inspectable_list}')
odd_elem_sum = 0
print('На нечётных позициях элементы ', end = '')
for item in range(len(inspectable_list) - 1):
    if item % 2 != 0:
        odd_elem_sum += inspectable_list[item]
        print(f'{inspectable_list[item]}, ', end = '')
print(f' их сумма = {odd_elem_sum}')