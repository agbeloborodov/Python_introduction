''' Задание 8_2. Нужно напистаь программу. В ней используем классы - имя студента name, номер группы group и список полученных оценок progress.
В самой программе вводим список всех студентов. В программе нужно вывести список студентов, отсортированный по имени, А так же студентов, у которых низкие оценки'''

from statistics import mean                                             # Для удобочитаемости

class Student:                                                          # Ненужное и не стал инициализировать
    def __init__(self, list_students):
        self.list_students = list_students

    def name_sorted(self, list_students):                               # Сортировка по имени в алфавитном порядке
        self.name = [x[0] for x in list_students]
        print('Список студентов, отсортированный по имени:')
        print(f'{sorted(self.name)}')

    def bad_slow_student(self, list_students):                          # Сортировка всего списка по среднему значению списка оценок отдельн(ого)(ой) студент(а)(ки)
        self.progress = [round(mean(x[2])) for x in list_students]
        print('Список студентов, у которых низкие оценки:')
        for i in range(len(self.progress)):
            list_students[i][2] = self.progress[i]
            if (list_students[i][2] <= 3):
                print(f' У студента {list_students[i][0]} из группы {list_students[i][1]} средняя оценка не превышает {list_students[i][2]} ')


def print_list(any_list):                                               # Функция вывода данных по студентам  в консоль
    for row in any_list:
        for item in row:
            print(f'{item}\t' , end = "" )
        print()

list_students = [                                                       # Всё по условию задачи, не так ли?
    ['Anna', '26b', [5, 5, 4, 5, 4, 5, 5, 4, 5]],
    ['Bob', '12c', [3, 3, 4, 2, 3, 3]],
    ['John', '38q', [2, 1, 3, 2, 1, 1]],
    ['Jenny', '11e', [5, 3, 3, 4, 2, 3, 3, 2, 3]],
    ['Carl', '43a', [5, 5, 5, 5, 5, 5, 5, 5, 5]],
    ['Bad_boy', '11z', [1, 2, 1, 1, 1, 1]]
    ]
print('Исходный список в формате [Имя, Группа, Список оценок]: ')       # Отсюда и далее:  юзер-интерфейс
print_list(list_students)
print()
any_object = Student(list_students)                                     # Создаём экземпляр класса
any_object.name_sorted(list_students)                                   # Сортировка списка по имени методом класса
print()
any_object.bad_slow_student(list_students)                              # Сортировка списка по неуспеваемости методом класса
print()