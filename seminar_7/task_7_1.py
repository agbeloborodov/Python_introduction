''' Задача 7_1.  Создать консольного бота, админящего недельное расписание задач  '''

import datetime


def conv_file_name(current_day):               # Формирование имени файла
    file_name = current_day + '.txt'
    return file_name

def current_tasks(current_day):                # Функция просмотра текущих задач на сегодня
    with open(conv_file_name(current_day), 'r') as my_file:
        print(my_file.read())

def task_corrrection(current_day):             # Функция коррекции текущих задач на сегодня
    with open(conv_file_name(current_day), 'r') as my_file:
        temp_list_str = my_file.readlines()
    temp_dictionary = dict([x.split('.') for x in temp_list_str])
    print('Выберите номер задачи, которую хотите скорректировать (1 или 2 или .... ) :  ', end = '')
    temp_key = input()
    print('Введите новую задачу в формате  "00:00 - 23:59"  Делаю то-то :  ')
    temp_value = input() + '\n'
    temp_dictionary[temp_key] = ' ' + temp_value
    temp_list = list(temp_dictionary.items())
    temp_list_str = list('.'.join(x) for x in  temp_list)
    with open(conv_file_name(current_day), 'w') as my_file:
       my_file.writelines(line for line in temp_list_str)

def task_adding(current_day):                  # Функция добавления текущих задач на сегодня
    with open(conv_file_name(current_day), 'r') as my_file:
        temp_list_str = my_file.readlines()
    temp_dictionary = dict([x.split('.') for x in temp_list_str])
    temp_key = str(len(temp_dictionary) + 1)
    print('Введите новую задачу в формате  "00:00 - 23:59"  Делаю то-то :  ')
    temp_value = input() + '\n'
    temp_dictionary[temp_key] = ' ' + temp_value
    temp_list = list(temp_dictionary.items())
    temp_list_str = list('.'.join(x) for x in  temp_list)
    with open(conv_file_name(current_day), 'w') as my_file:
       my_file.writelines( line for line in temp_list_str )

def task_delete(current_day):                  # Функция удаления текущих задач на сегодня
    with open(conv_file_name(current_day), 'r') as my_file:
        temp_list_str = my_file.readlines()
    temp_dictionary = dict([x.split('.') for x in temp_list_str])
    print('Выберите номер задачи, которую хотите удалить (1 или 2 или .... ) :  ', end = '')
    temp_key = input()
    del temp_dictionary[temp_key]
    temp_list = list(temp_dictionary.items())
    temp_list_str = list('.'.join(x) for x in  temp_list)
    with open(conv_file_name(current_day), 'w') as my_file:
       my_file.writelines(line for line in temp_list_str)

def bot_admin():                               # Интерфейс админ-бота
    current_day = datetime.datetime.today().strftime('%A')
    print(f"Сегодня {current_day}")
    while True:
        print('Выберите то, что Вам угодно: (рекомендую сначала взглянуть на текущие задачи - пункт 1)')
        print('1 - взглянуть на текущие задачи, 2 - скорректировать их, 3 - добавить задачу, 4 - удалить задачу, Q - выход из программы :  ', end = '')
        input_key = input()
        if input_key == 'Q' or input_key == 'q' or input_key == 'Й' or input_key == 'й':
            break
        elif input_key == '1':
            current_tasks(current_day)
            continue
        elif input_key == '2':
            task_corrrection(current_day)
            continue
        elif input_key == '3':
            task_adding(current_day)
            continue
        elif input_key == '4':
            task_delete(current_day)
            continue
        else:
            continue

bot_admin()