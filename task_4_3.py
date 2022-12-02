''' Задача 4_3.    Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию методом сортировки выбором.'''

import random

def create_random_list(lenght = 10, lower_limit = -100, upper_limit = 100):     # Функция задания списка из случайных чисел
    created_list = []
    for item in range (lenght):
        random.randint(lower_limit, upper_limit)
        created_list.append(random.randint(lower_limit, upper_limit))
    return created_list

inspectable_list = create_random_list(30)
print('Сгенерированный список выглядит следующим образом:')
print(inspectable_list)
print('Отсортированный список по возрастанию методом сортировки выбором выглядит следующим образом:')
for item in range(0, len(inspectable_list) - 1):
    var_mininmum = item
    for jtem in range(item + 1, len(inspectable_list)):
        if inspectable_list[jtem] < inspectable_list[var_mininmum]:
            var_mininmum = jtem
    inspectable_list[item], inspectable_list[var_mininmum] = inspectable_list[var_mininmum], inspectable_list[item]
print(inspectable_list)