''' Задача 2_3. Вводим с клавиатуры целое число - это зарплата. Нужно вывести в консоль -  минимальное кол-во купюр, которыми можно выдать ЗП.
И сколько, и каких бухгалтер выдаст 25-рублевых купюр, 10-рублевых, 3-рублевых и 1-рублевых.
З.Ы. Исключительно некрасивое решение, но как это дело оформить по Zen (т.е. в цикле), не используя список  - ума не приложу'''

salary = int(input('Введите натуральное число (зарплата в рублях): '))
print(f'Будет выдано {salary // 25} таньга по 25 рублей, ',end = '')
salary = salary % 25
print(f'{salary // 10} таньга по 10 рублей, ',end = '')
salary = salary % 10
print(f'{salary // 3} таньга по 3 рубля, ',end = '')
salary = salary % 3
print(f'{salary // 1} таньга по 1 рублю')