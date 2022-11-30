'''  Задание 3.10.  Вводим с клавиатуры десятичное число. Необходимо перевести его в шестнадцатиричную систему счисления.'''

#   Вариант №1
dec_number = int(input('Введите натуральное число в десятичной системе счисления (dec): '))     # Канонично
temp_str = ''
hex_str = '0123456789ABCDEF'
print(f'{dec_number} (dec) = ', end='')
while dec_number > 0:
    temp_str = hex_str[dec_number % 16] + temp_str
    dec_number = dec_number // 16
print(f'{temp_str} (hex)')

#   Вариант №2
# dec_number = int(input('Введите натуральное число в десятичной системе счисления (dec): '))   # Элегантно
# hex_number = (f'{dec_number:x}').upper()
# print(f'{dec_number} (dec) = {hex_number} (hex)')

#   Вариант №3
# print(hex(int(input('Введите натуральное число в десятичной системе счисления (dec):')))[2:].upper())   # Zen of Python?