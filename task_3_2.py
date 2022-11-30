'''  Задание 3.11.  Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом.'''

# Очень много времени потрачено на эксперименты с isdigit(), isnumeric(), float(input_str).is_integer() и т.д. Скорее всего, простое и элегантное решение прошло мимо меня.
# Поэтому - вот так:
def is_float(any_str):
    try:
        float(any_str)
        if (any_str.count('.') == 1):
            return print('Это дробное число')
        else:
            return print('Это НЕ дробное число')
    except ValueError:
        return print('Это НЕ дробное число')
input_str = input('Введите исследуемую строку: ')
is_float(input_str)