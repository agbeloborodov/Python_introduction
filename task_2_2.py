''' Задача 2_2.	Вводим с клавиатуры целое число X. Далее вводим Х целых чисел.
Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел. '''

sequence_weight = int(input('Введите количество элементов последовательности целых чисел: '))
great_max = max_second = float('-inf')
for item in range(sequence_weight):
    sequence_element = int(input(f'Введите {item + 1} элемент последовательности: '))
    if (item == 0): great_max = sequence_element
    else:
        if (sequence_element > great_max):
            max_second = great_max
            great_max = sequence_element
        elif (sequence_element > max_second):
            max_second = sequence_element
print(f'Первое максимальное число = {great_max}, второе максимальное число = {max_second}')