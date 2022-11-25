'''   Задача 2_4. Вводим с клавиатуры многозначное число. Необходимо узнать и сказать последовательность цифр этого числа при просмотре слева направо упорядочена по возрастанию или нет.
Например 1579 - да ( 1 меньше 5, 5 меньше 7, а 7 меньше 9), 1427 - нет.'''

sequense_string = input('Введите исследуемое число произвольной длины: ')
sequence_numbers = int(sequense_string)
result = True
while sequence_numbers // 10 != 0:
    temp_item = sequence_numbers % 10
    sequence_numbers = sequence_numbers // 10
    if temp_item <= sequence_numbers % 10:
       result = False
if (result): print(f'Число {sequense_string} упорядочено по возрастанию')
else: print(f'Число {sequense_string} НЕ упорядочено по возрастанию')