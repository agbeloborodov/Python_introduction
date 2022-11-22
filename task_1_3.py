''' Задача 1_3.	Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой
 находится эта точка (или на какой оси она находится).'''

x_coordinate = float(input('Введите координату точки по оси абцисс (X): '))
y_coordinate = float(input('Введите координату точки по оси ординат (Y): '))
if (x_coordinate == 0 and y_coordinate ==0):
    print(f'Заданная точка X={x_coordinate}, Y={y_coordinate} - начало начал, не находящееся ни в одной четверти декартовой системы координат')
elif (x_coordinate > 0 and y_coordinate > 0):
    print(f'Заданная точка X={x_coordinate}, Y={y_coordinate} находится в I четверти декартовой системы координат')
elif (x_coordinate < 0 and y_coordinate > 0):
    print(f'Заданная точка X={x_coordinate}, Y={y_coordinate} находится во II четверти декартовой системы координат')
elif (x_coordinate < 0 and y_coordinate < 0):
    print(f'Заданная точка X={x_coordinate}, Y={y_coordinate} находится в III четверти декартовой системы координат')
elif (x_coordinate > 0 and y_coordinate < 0):
    print(f'Заданная точка X={x_coordinate}, Y={y_coordinate} находится в IV четверти декартовой системы координат')
elif (x_coordinate == 0 and y_coordinate != 0):
    print(f'Заданная точка X={x_coordinate}, Y={y_coordinate} находится на оси абцисс')
elif (x_coordinate != 0 and y_coordinate == 0):
    print(f'Заданная точка X={x_coordinate}, Y={y_coordinate} находится на оси ординат')