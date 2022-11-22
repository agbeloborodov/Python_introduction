''' Задача 1_5.	Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.'''

x_a_coordinate = float(input('Введите координату точки A по оси абцисс (Xa): '))
y_a_coordinate = float(input('Введите координату точки A по оси ординат (Ya):'))
x_b_coordinate = float(input('Введите координату точки B по оси абцисс (Xb):'))
y_b_coordinate = float(input('Введите координату точки B по оси ординат (Yb):'))
distance_a_to_b = ((x_b_coordinate - x_a_coordinate)**2  + (y_b_coordinate - y_a_coordinate)**2)**0.5   #Чтобы не подключать функцию sqrt() из библиотеки math
print(f'Расстояние между точками А ({round(x_a_coordinate,2)}, {round(y_a_coordinate,2)}) и B ({round(x_b_coordinate,2)}, {round(y_b_coordinate,2)}) равно {round(distance_a_to_b,4)}')