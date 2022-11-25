''' Задача 2_1.  Вводим с клавиатуры целое число X и У. Выводим на экран количество чисел между Х и У, которые делятся на 2 и 3 '''

low_limit = int(input('Введите целое число X (нижнюю границу диапазона): '))
high_limit = int(input('Введите целое число Y (вернюю границу диапазона): '))
count_numbers = 0
print(f'Между X={low_limit} и Y={high_limit} находятся следующие числа, которые делятся на 2 и 3: ', end='')
for item in range(low_limit, high_limit):
    if (item % 2 == 0) and (item % 3 == 0):
        print(f'{item}  ', end='')
        count_numbers += 1
print(f'\nТаким образом, в указанном промежутке между {low_limit} и {high_limit} имеют место быть {count_numbers} чисел, удовлетворяющих условию задачи')